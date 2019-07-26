from Game import Game
from Pokemon import Pokemon 
from random import randrange
import database_client
import json

def __get_battle_number():
    counter = database_client.get_counter_collection()
    battle_number = counter.find_and_modify(
        query={"_id":"battles"},
        update={"$inc":{"sequence_value":1}})
    return battle_number['sequence_value']

def is_playable():
    alive_pokemon = __get_alive_pokemon()
    return alive_pokemon.count() > 1

def __get_alive_pokemon():
    game_collection = database_client.get_game_collection()
    query = {"alive":True}
    alive_pokemon = game_collection.find(query)
    return alive_pokemon

def play():
    wrestlers = __get_wrestlers()
    w = wrestlers[0]
    winner = Pokemon(w['number'],w['name'],w['alive'])
    l = wrestlers[1]
    loser = Pokemon(l['number'],l['name'],l['alive'])
    battle_number = __get_battle_number()
    alive_number = __get_alive_pokemon().count()
    return Game(battle_number, alive_number, winner, loser)

def __get_wrestlers():
    alive_pokemon = __get_alive_pokemon()
    idxs = []
    values = []
    for idx, val in enumerate(alive_pokemon):
        idxs.append(idx)
        values.append(val)
    p1 = idxs.pop(randrange(len(idxs)))
    p2 = idxs.pop(randrange(len(idxs)))
    winner = values[p1]
    loser = values[p2]
    loser = __update_loser(loser)
    return [winner, loser]

def __update_loser(loser):
    loser['alive'] = False
    game_collection = database_client.get_game_collection()
    game_collection.find_and_modify(
        query={"_id":loser["_id"]},
        update=loser)
    return loser

def has_ended():
    return __get_alive_pokemon().count() == 1

def get_winner():
    return __get_alive_pokemon()[0]

def reset_game():
    game = database_client.get_game_collection()
    game.update_many({}, {"$set": {"alive": True}})
    counter = database_client.get_counter_collection()
    counter.update_many({}, {"$set": {"sequence_value": 1}})

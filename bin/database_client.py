from pymongo import MongoClient
import os

def __get_client():
    client = MongoClient(os.environ.get("MONGO_DB_URI"))
    return client

def get_game_collection():
    client = __get_client()
    return client['pokemon-war-bot']['game']

def get_counter_collection():
    client = __get_client()
    return client['pokemon-war-bot']['counters']

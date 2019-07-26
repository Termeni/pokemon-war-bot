from PIL import Image
import twitter
import os.path
import boto3
import requests
from io import BytesIO
from io import StringIO

def __get_api():
    consumer_key = os.environ.get("TW_KEY")
    consumer_secret = os.environ.get("TW_SECRET")
    access_token_key = os.environ.get("TW_AT_KEY")
    access_token_secret = os.environ.get("TW_AT_SECRET")

    api = twitter.Api(consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret)
    return api

def publish_status(result):
    api = __get_api()
    file1 = os.environ.get("SERVER_URL") + "/img/publish/battle.png"
    file2 = os.environ.get("SERVER_URL") + "/img/publish/status.png"
    api.PostUpdate(result.get_game_description(), media=[file1,file2])

def publish_winner(winner):
    template = ("Incredible!\n"
        + "#{name} is the strongest #CyberPokemon!\n"
        + "#Pokemons and humans have hope in the future again!\n"
        + "You're breathtaking!\n" 
        + "#PokemonWarBot #WarBot #Cyberpunk")
    winner_post = template.format(name=winner['name'])
    print(winner_post)
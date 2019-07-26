from PIL import Image
from io import BytesIO
from Pokemon import Pokemon
import boto3
import requests
import amazon_client
import database_client
import multiprocessing

def update_status_images(game):
    __update_battle_image(game)
    __updte_status_image()

def __update_battle_image(game):
    img1 = open_image(game.winner.get_full_image_path())
    img2 = open_image(game.loser.get_full_image_path())
    images = [img1,img2]

    scale_images(images)
    new_im = join_images(images)
    amazon_client.update_battle_image(new_im)

def scale_images(images):
    img1 = images[0]
    img2 = images[1]
    if img2.size[1] > img1.size[1]:
        img2.thumbnail((img2.size[0],img1.size[1]), Image.ANTIALIAS)
    else:
        img1.thumbnail((img1.size[0],img2.size[1]), Image.ANTIALIAS)

def join_images(images):
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGBA', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    return new_im

def __updte_status_image():
    game = database_client.get_game_collection()
    pokemons = game.find().sort("number",1)
    sprites_urls = [
        (int(p['number']),Pokemon(p['number'], p['name'], p['alive']).get_sprites_path()) 
        for p in pokemons
        ]
    pool = multiprocessing.Pool(7)
    sprites = list(pool.map(index_and_open_image, sprites_urls))
    sorted_sprites = sorted(sprites, key=lambda sprite: sprite[0])
    img = generate_status_image(sorted_sprites)
    amazon_client.update_status_image(img)

def index_and_open_image(tuple):
    return (tuple[0], open_image(tuple[1]))

def open_image(url):
    return Image.open(BytesIO(requests.get(url).content))

def generate_status_image(sprites):
    new_im = Image.new('RGBA', (800, 1230))
    x_offset = 0
    y_offset = 0
    for i in sprites:
        new_im.paste(i[1], (x_offset,y_offset))
        x_offset += 40
        if i[0]%20 == 0:
            y_offset += 30
            x_offset = 0
    return new_im


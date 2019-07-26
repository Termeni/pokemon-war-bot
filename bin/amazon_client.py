from io import BytesIO
import boto3
import os

def __get_client():
    client = boto3.client('s3',aws_access_key_id=os.environ.get("AWS_KEY"),
        aws_secret_access_key=os.environ.get("AWS_SECRET"))
    return client
    

def update_battle_image(img):
    out_img = BytesIO()
    img.save(out_img,'PNG')
    out_img.seek(0)
    client = __get_client()
    client.put_object(Body=out_img, Bucket='pokemon-war-bot', Key='img/publish/battle.png')

def update_status_image(img):
    out_img = BytesIO()
    img.save(out_img,'PNG')
    out_img.seek(0)
    client = __get_client()
    client.put_object(Body=out_img, Bucket='pokemon-war-bot', Key='img/publish/status.png')

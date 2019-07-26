import os

class Pokemon:

    img_path = os.environ.get("SERVER_URL") + "/img"
    full = "/full"
    sprites = "/sprites"

    def __init__(self, number, name, alive):
        self.number = number
        self.name = name
        self.alive = alive

    def get_full_image_path(self):
        return (self.img_path + self.full + "/" + self.number + "_" + self.name 
            + (".jpg" if self.alive else "_ko.png"))

    def get_sprites_path(self):
        return (self.img_path + self.sprites + "/" + self.number 
            + (".png" if self.alive else "_ko.png"))
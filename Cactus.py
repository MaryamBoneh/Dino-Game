import arcade, random

class Cactus(arcade.Sprite):
    def __init__(self, w):
        super().__init__()
        self.picture = random.choice(['img/cactus1.png', 'img/cactus2.png', 'img/cactus3.png'])
        self.texture = arcade.load_texture(self.picture)
        self.center_x = w + 30
        self.center_y = 125
        self.change_x = -6
        self.change_y = 0
        self.scale = 0.3

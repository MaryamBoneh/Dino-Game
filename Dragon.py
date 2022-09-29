import arcade, random

class Dragon(arcade.AnimatedWalkingSprite):
    def __init__(self, w):
        super().__init__()
        self.walk_right_textures = [arcade.load_texture('img/enemy-bird-0.png'), arcade.load_texture('img/enemy-bird-1.png')]
        self.center_x = w + 30
        self.center_y = random.randint(220, 300)
        self.change_x = -6
        self.change_y = 0
        self.scale = 0.7

    def flapping(self, s):
        if s % 2 == 0:
            self.texture = arcade.load_texture('img/enemy-bird-0.png')
        else:
            self.texture = arcade.load_texture('img/enemy-bird-1.png')

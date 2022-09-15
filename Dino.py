import arcade

class Dino(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.walk_right_textures = [arcade.load_texture('img/dino-walk-0.png'), arcade.load_texture('img/dino-walk-1.png')]
        self.walk_down_textures = [arcade.load_texture('img/dino-down-0.png'), arcade.load_texture('img/dino-down-1.png')]
        self.walk_up_textures = [arcade.load_texture('img/dino-walk-1.png')]
        self.walk_down_textures = [arcade.load_texture('img/dino-walk-0.png')]
        self.center_x = 200
        self.center_y = 220
        self.change_x = 1
        self.change_y = -6
        self.scale = 0.3
        self.bent = 0

    def show_walking(self, s):
        if s % 2 == 0:
            self.texture = arcade.load_texture('img/dino-walk-0.png')
        else:
            self.texture = arcade.load_texture('img/dino-walk-1.png')

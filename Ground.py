import arcade, random

class Ground(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.picture = random.choice(['img/ground-0.png', 'img/ground-1.png', 'img/ground-2.png',
                                     'img/ground-3.png', 'img/ground-4.png', 'img/ground-5.png', 'img/ground-6.png'])
        self.texture = arcade.load_texture(self.picture)
        self.center_x = width
        self.center_y = height
        self.change_x = -6
        self.change_y = 0
        self.width = 132
        self.height = 56

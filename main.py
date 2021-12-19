import arcade, random
import webcam


class Game(arcade.Window):
    def __init__(self):
        self.w = 900
        self.h = 400
        self.msec = 0
        self.gravity = 0.5
        super().__init__(self.w, self.h, "Dino")
        arcade.set_background_color(arcade.color.WHITE)
        self.dino = Dino()
        self.grounds = arcade.SpriteList()
        self.cactuses = arcade.SpriteList()

        for i in range(0, self.w + 132, 132):
            ground = Ground(i, 50)
            self.grounds.append(ground)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.dino, self.grounds, self.gravity)

    def on_draw(self):
        arcade.start_render()
        for ground in self.grounds:
            ground.draw()

        for cactus in self.cactuses:
            cactus.draw()

        self.dino.draw()

    def on_update(self, delta_time: float):
        self.physics_engine.update()

        self.dino.center_x = 200
        self.msec += 0.5
        self.dino.show_walking(self.msec)

        if webcam.check():
            if self.physics_engine.can_jump():
                self.dino.change_y = 12

        for ground in self.grounds:
            if ground.center_x < 0:
                self.grounds.remove(ground)
                self.grounds.append(Ground(self.w + 132, 50))

        if random.random() < 0.1:
            self.cactuses.append(Cactus())
            print('cactuuussss')



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


class Cactus(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.picture = random.choice(['img/cactus1.png', 'img/cactus2.png', 'img/cactus3.png'])
        self.texture = arcade.load_texture(self.picture)
        self.center_x = 800
        self.center_y = 100
        self.change_x = -6
        self.change_y = 0
        self.scale = 0.3


class Dino(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.walk_right_textures = [arcade.load_texture(
            'img/dino-walk-0.png'), arcade.load_texture('img/dino-walk-1.png')]
        self.walk_down_textures = [arcade.load_texture(
            'img/dino-down-0.png'), arcade.load_texture('img/dino-down-1.png')]
        self.walk_up_textures = [arcade.load_texture('img/dino-walk-1.png')]
        self.walk_down_textures = [arcade.load_texture('img/dino-walk-0.png')]
        self.center_x = 200
        self.center_y = 233
        self.change_x = 1
        self.change_y = 0
        self.scale = 0.3
        self.bent = 0

    def show_walking(self, s):
        if s % 2 == 0:
            self.texture = arcade.load_texture('img/dino-walk-0.png')
        elif s % 3 == 0:
            self.texture = arcade.load_texture('img/dino-walk-1.png')


if __name__ == '__main__':
    game = Game()
    arcade.run()

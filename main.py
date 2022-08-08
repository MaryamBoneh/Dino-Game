import arcade, random, time
import webcam


class Game(arcade.Window):
    def __init__(self):
        self.w = 900
        self.h = 400
        self.msec = 0
        self.gravity = 0.9
        self.game_over = False
        super().__init__(self.w, self.h, "Dino")
        arcade.set_background_color(arcade.color.WHITE)
        self.dino = Dino()
        self.grounds = arcade.SpriteList()
        self.cactuses = arcade.SpriteList()
        self.cactus_create_at = time.time()

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
        now = time.time()
        self.physics_engine.update()

        self.dino.center_x = 200
        self.msec += 1
        self.dino.show_walking(self.msec)

        if webcam.check():
            if self.physics_engine.can_jump():
                self.dino.change_y = 15

        if random.random() < 0.02 and (now - self.cactus_create_at > 3):
            self.cactuses.append(Cactus(self.w))
            self.cactus_create_at = time.time()

        for cactus in self.cactuses:
            cactus.update()
            if cactus.center_x < 0:
                self.cactuses.remove(cactus)

            if arcade.check_for_collision(self.dino, cactus):
                self.game_over = True

        for ground in self.grounds:
            if ground.center_x < 0:
                self.grounds.remove(ground)
                self.grounds.append(Ground(self.w + 132, 50))


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


if __name__ == '__main__':
    game = Game()
    arcade.run()

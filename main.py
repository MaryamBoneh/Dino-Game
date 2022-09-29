import arcade, random, time
import webcam
from Dino import Dino
from Ground import Ground
from Cactus import Cactus
from Dragon import Dragon


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
        self.dragons = arcade.SpriteList()
        self.cactus_create_at = time.time()
        self.dragon_create_at = time.time()

        for i in range(0, self.w + 132, 132):
            ground = Ground(i, 50)
            self.grounds.append(ground)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.dino, self.grounds, self.gravity)

    def on_draw(self):

        arcade.start_render()

        if self.game_over:
            self.dino.opps()
            arcade.draw_text('Game Over', 150, self.h//2, arcade.color.RED, 60, width=600, font_name='Kenney Mini Square', align='center')
            arcade.draw_text('please press "ENTER" key to reset', 150, self.h//3, arcade.color.DARK_RED, 24, width=600, font_name='Kenney Mini Square', align='center')
        else:
            for ground in self.grounds:
                ground.draw()

            for cactus in self.cactuses:
                cactus.draw()

            for dragon in self.dragons:
                dragon.draw()

        self.dino.draw()

    def on_update(self, delta_time: float):
        now = time.time()
        self.physics_engine.update()

        self.dino.center_x = 200
        self.msec += 1

        if not self.game_over:
            self.dino.show_walking(self.msec)
            if webcam.check():
                if self.physics_engine.can_jump():
                    self.dino.change_y = 15

            if random.random() < 0.025 and (now - self.cactus_create_at > 3):
                self.cactuses.append(Cactus(self.w))
                self.cactus_create_at = time.time()

            for cactus in self.cactuses:
                cactus.update()
                if cactus.center_x < 0:
                    self.cactuses.remove(cactus)

                if arcade.check_for_collision(self.dino, cactus):
                    self.game_over = True
            
            if self.msec > 300:
                if random.random() < 0.025 and (now - self.dragon_create_at > 3):
                    self.dragons.append(Dragon(self.w))
                    self.dragon_create_at = time.time()

                for dragon in self.dragons:
                    dragon.flapping(self.msec)
                    dragon.update()
                    if dragon.center_x < 0:
                        self.dragons.remove(dragon)

            for ground in self.grounds:
                if ground.center_x < 0:
                    self.grounds.remove(ground)
                    self.grounds.append(Ground(self.w + 132, 50))


    def on_key_press(self, key, modifiers):
        if key==arcade.key.ENTER and self.game_over:
            self.game_over = False

if __name__ == '__main__':
    game = Game()
    arcade.run()

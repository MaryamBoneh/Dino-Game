import arcade, random
import cv2 
import mediapipe as mp
from math import hypot
import numpy as np 


class Game(arcade.Window):
    def __init__(self):
        self.w = 900
        self.h = 400
        self.msec = 0
        self.gravity = 0.5
        super().__init__(self.w , self.h ,"Dino")
        arcade.set_background_color(arcade.color.WHITE)
        self.dino = Dino()
        self.grounds = arcade.SpriteList()
        self.cap = cv2.VideoCapture(0)
        self.mpHands = mp.solutions.hands 
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

        for i in range(0, self.w + 132, 132):
            ground = Ground(i, 50)
            self.grounds.append(ground)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.dino, self.grounds, self.gravity)


    def on_draw(self):
        arcade.start_render()
        for ground in self.grounds:
            ground.draw()

        self.dino.draw()
   

    def on_update(self, delta_time: float):
        self.physics_engine.update()
        self.dino.update_animation()

        self.dino.center_x = 200
        self.msec += 0.5
        self.dino.show_walking(self.msec)

        success,img = self.cap.read()
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        lmList = []
        if results.multi_hand_landmarks:
            for handlandmark in results.multi_hand_landmarks:
                for id,lm in enumerate(handlandmark.landmark):
                    h,w,_ = img.shape
                    cx,cy = int(lm.x*w),int(lm.y*h)
                    lmList.append([id,cx,cy]) 
                self.mpDraw.draw_landmarks(img,handlandmark,self.mpHands.HAND_CONNECTIONS)

        if lmList != []:
            x1,y1 = lmList[4][1], lmList[4][2]
            x2,y2 = lmList[8][1], lmList[8][2]
            x3,y3 = lmList[12][1], lmList[12][2]
            x4,y4 = lmList[16][1], lmList[16][2]
            x5,y5 = lmList[20][1], lmList[20][2]

            length54 = hypot(x5-x4 , y5-y4)
            length43 = hypot(x4-x3 , y4-y3)
            length32 = hypot(x3-x2 , y3-y2)
            length21 = hypot(x2-x1 , y2-y1)

            if length21 < 50 and length32 < 50 and length43 < 50 and length54 < 50:
                if self.physics_engine.can_jump():
                    self.dino.change_y = 15
            
        cv2.imshow('Image',img)

        for ground in self.grounds:
            if ground.center_x < 0:
                self.grounds.remove(ground)
                self.grounds.append(Ground(self.w + 132 ,50))


class Ground(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.picture = random.choice(['img/ground-0.png','img/ground-1.png', 'img/ground-2.png', 'img/ground-3.png', 'img/ground-4.png', 'img/ground-5.png', 'img/ground-6.png'])
        self.texture = arcade.load_texture(self.picture)
        self.center_x = width
        self.center_y = height
        self.change_x = -6
        self.change_y = 0
        self.width = 132
        self.height = 56


class Dino(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.walk_right_textures = [arcade.load_texture('img/dino-walk-0.png'), arcade.load_texture('img/dino-walk-1.png')]
        self.walk_down_textures = [arcade.load_texture('img/dino-down-0.png'), arcade.load_texture('img/dino-down-1.png')]
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
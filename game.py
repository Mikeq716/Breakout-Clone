import pygame
import os
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick

class Game:
    def game_loop(self, paddle, ball):
        Clock = pygame.time.Clock()
        red_row = self.create_row(100, brick_red_img)
        yellow_row = self.create_row(122, brick_yellow_img)
        pink_row = self.create_row(144, brick_pink_img)
        green_row = self.create_row(166, brick_green_img)
        purple_row = self.create_row(188, brick_purple_img)
        blue_row = self.create_row(210, brick_blue_img)
        orange_row = self.create_row(232, brick_orange_img)

        Run = True
        while Run:
            delta = Clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False

            SCREEN.fill((0, 0, 0))

            paddle.update(delta, ball)
            ball.update(delta)
            
            self.update_brick_list(red_row, ball, delta)
            self.update_brick_list(yellow_row, ball, delta)
            self.update_brick_list(pink_row, ball, delta)
            self.update_brick_list(green_row, ball, delta)
            self.update_brick_list(purple_row, ball, delta)
            self.update_brick_list(blue_row, ball, delta)
            self.update_brick_list(orange_row, ball, delta)

            pygame.display.update()

    def create_row(self, y, img):
        new_row = []
        x = 54
        for i in range(16):
            new_row.append(Brick(x, y, img))
            x += 54
        return new_row

    def update_brick_list(self, new_list, ball, delta):
        for obj in new_list:
            obj.update(ball, delta)
            if obj.hit == True:
                new_list.remove(obj)
import pygame
import os
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick

class Game:
    def game_init(self):
        pygame.init()
        pygame.display.set_caption("Breakout")
        pygame.mouse.set_visible(0)

    def game_loop(self, paddle, ball):
        Clock = pygame.time.Clock()
        Rows = []
        ball_active = True

        GameHelper.load_level(20, Rows)
        
        Run = True
        while Run:
            delta = Clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ball_active = False

            GameHelper.update(Rows, ball, delta, paddle)


class GameHelper:
    def load_level(y, Rows):
        row = []
        with open(os.path.join('levels', 'test_level.txt')) as level:
            lines = level.readlines()
        for obj in lines:
            x = 21
            new_row = []
            row = obj.join('')
            row = obj.split(',')
            for img in row:
                if int(img) == 0:
                    x += 54
                    continue
                new_row.append(Brick(x, y, IMAGES[int(img)]))
                x += 54
            y += 22
            Rows.append(new_row)

    def update_brick_list(Rows, ball, delta):
        for row in Rows:
            for brick in row:
                brick.update(ball, delta)
                if brick.hit == True:
                    row.remove(brick)

    def update(rows, ball, delta, paddle):
        SCREEN.fill((0, 0, 0))
        paddle.update(delta, ball)
        ball.update(delta, paddle)
        GameHelper.update_brick_list(rows, ball, delta)   
        pygame.display.update()

    
    

    
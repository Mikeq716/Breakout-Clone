import pygame
import os
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick

class Game:
    def game_loop(self, paddle, ball):
        Clock = pygame.time.Clock()
        fresh_ball = True
        Rows = []
        self.load_level(20, Rows)
        
        Run = True
        while Run:
            delta = Clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        fresh_ball = False

            SCREEN.fill((0, 0, 0))

            paddle.update(delta, ball)
            ball.update(delta, paddle, fresh_ball)

            for row in Rows:
                self.update_brick_list(row, ball, delta)
            
            if ball.position.y + ball.direction.y * BALL_SPEED * delta >= SCREEN_HEIGHT:
                fresh_ball = True
            
            pygame.display.update()

    def load_level(self, y, Rows):
        row = []
        with open(os.path.join('levels', 'test_level.txt')) as level:
            lines = level.readlines()
        for obj in lines:
            x = 21
            new_row = []
            row = obj.join('')
            row.strip()
            row = obj.split(',')
            for img in row:
                new_row.append(Brick(x, y, IMAGES[int(img)]))
                x += 54
            y += 22
            Rows.append(new_row)


    def update_brick_list(self, new_list, ball, delta):
        for obj in new_list:
            obj.update(ball, delta)
            if obj.hit == True:
                new_list.remove(obj)

    
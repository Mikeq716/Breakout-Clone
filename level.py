import pygame
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from scorecard import Scorecard

class Level:
    current_level = 0

    def update_level(ball, delta, level, Rows):
        for row in Rows:
            if len(row) == 0:
                Rows.remove(row)     
            for brick in row:
                brick.update(ball, delta)
                if brick.hit == True:
                    row.remove(brick)

    def is_level_done(Rows, ball):
        if len(Rows) == 0:
            Level.current_level += 1
            Level.__new_level(Level.current_level, Rows)
            ball.ball_active = False

    def __new_level(level, Rows):
        pygame.time.delay(300)
        Level.__load_level(50, Rows, Level.current_level)

    def __select_level(level):
        return 'level' + str(level) + '.txt'

    def __load_level(y, Rows, level):
        row = []
        with open(os.path.join('levels', Level.__select_level(level))) as level:
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
                new_row.append(Brick(x, y, IMAGES[int(img)], BRICK_VALUES[int(img)]))
                x += 54
            y += 22
            Rows.append(new_row)

    
    
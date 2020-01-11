import pygame
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from scorecard import Scorecard

class Level:
    current_level = 0

    def new_level(level, Rows):
        pygame.time.delay(300)
        Level.current_level += 1
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

    
    
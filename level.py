import pygame
import os
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick

class Level:
    def load_level(y, Rows, level):
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
                new_row.append(Brick(x, y, IMAGES[int(img)]))
                x += 54
            y += 22
            Rows.append(new_row)

    def update_level(Rows, ball, delta, level):
        for row in Rows:
            if len(row) == 0:
                Rows.remove(row)
                
            for brick in row:
                brick.update(ball, delta)
                if brick.hit == True:
                    row.remove(brick)
            

    def __select_level(level):
        return 'level' + str(level) + '.txt'

    
    
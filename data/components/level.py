import pygame, os

from .. import config
from ..components.brick import *

class Level:
    #Function New Level
    #Function New Level adds 1 to the current level and then loads the new level
    def new_level(level, Rows):
        level += 1
        Rows.clear()
        Level.__load_level(50, Rows, level)


    #Function Select Level
    #Function Select Level returns a string containing the name of the txt file containing the level to be opened
    def __select_level(level):
        return 'level' + str(level) + '.txt'

    #Function Load Level
    #Function Load Level loads the level from the text file containing it
    def __load_level(y, Rows, level):
        config.CURRENT_COUNT = 0   
        with open(os.path.join('resources/levels', Level.__select_level(level))) as level:
            lines = level.readlines()
        for line in lines:
            x = 21
            new_row = []
            row = line.split(',')
            for obj in row:
                brick = obj.split('-')
                brick[1] = int(brick[1])
                if (brick[1]) == 0:
                    x += 54
                    continue
                if brick[0] == 'R':
                    value = BRICK_VALUES[brick[1]]
                    image = brick[1]
                elif brick[0] == 'L':
                    value = 0
                    image = brick[1] + 7
                new_row.append(BRICK_TYPE[brick[0]](x, y, IMAGES[image], value))
                x += 54
                if brick[0] == 'R':
                    Level.increase_count()
            y += 22
            Rows.append(new_row)

    def increase_count():
        config.CURRENT_COUNT += 1
    
IMAGES = {  1 : config.BRICK_IMGS['brick_blue_img'],
            2 : config.BRICK_IMGS['brick_green_img'],
            3 : config.BRICK_IMGS['brick_orange_img'],
            4 : config.BRICK_IMGS['brick_pink_img'],
            5 : config.BRICK_IMGS['brick_purple_img'],
            6 : config.BRICK_IMGS['brick_red_img'],
            7 : config.BRICK_IMGS['brick_yellow_img'],
            8 : config.BRICK_IMGS['brick_blue_locked_img'],
            9 : config.BRICK_IMGS['brick_green_locked_img'],
            10 : config.BRICK_IMGS['brick_orange_locked_img'],
            11 : config.BRICK_IMGS['brick_pink_locked_img'],
            12 : config.BRICK_IMGS['brick_purple_locked_img'],
            13 : config.BRICK_IMGS['brick_red_locked_img'],
            14 : config.BRICK_IMGS['brick_yellow_locked_img']
}
    
BRICK_TYPE = {  'R' : Brick,
                'L' : Locked_Brick
}
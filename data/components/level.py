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
            line = line.rstrip()
            x = 21
            new_row = []
            row = line.split(',')
            for brick in row:
                if brick == '0':
                    x += 54
                    continue
                new_row.append(Brick(x, y, IMAGES[brick], BRICK_VALUES[brick]))
                x += 54
                Level.increase_count()
            y += 22
            Rows.append(new_row)

    def increase_count():
        config.CURRENT_COUNT += 1
    
IMAGES = {  'BL' : config.BRICK_IMGS['brick_blue_img'],
            'GR' : config.BRICK_IMGS['brick_green_img'],
            'OR' : config.BRICK_IMGS['brick_orange_img'],
            'PI' : config.BRICK_IMGS['brick_pink_img'],
            'PU' : config.BRICK_IMGS['brick_purple_img'],
            'RE' : config.BRICK_IMGS['brick_red_img'],
            'YE' : config.BRICK_IMGS['brick_yellow_img'],
}
    
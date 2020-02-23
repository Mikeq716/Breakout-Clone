import pygame, os

from .. import config
from ..components.brick import Brick, BRICK_VALUES

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
        row = []
        with open(os.path.join('resources/levels', Level.__select_level(level))) as level:
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
                new_row.append(Brick(x, y, IMAGES[int(img)], BRICK_VALUES[int(img)], LOCKED[int(img)]))
                x += 54
                if int(img) < 8:
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

LOCKED = {  1 : False,
            2 : False,
            3 : False,
            4 : False,
            5 : False,
            6 : False,
            7 : False,
            8 : True,
            9 : True,
            10 : True,
            11 : True,
            12 : True,
            13 : True,
            14 : True
}

    
    
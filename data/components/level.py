import pygame, os

from .. import config
from ..components.brick import *

class Level:
    #Function New Level adds 1 to the current level and then loads the new level
    def new_level(level, Rows):
        Rows.clear()
        Level.__load_level(50, Rows, level)

    #Function Select Level returns a string containing the name of the txt file containing the level to be opened
    def __select_level(level):
        return 'level' + str(level) + '.txt'

    #Function Load Level loads the level from the text file containing it
    def __load_level(y, Rows, level):
        #Set Current Count of bricks to 0 for the current level
        config.CURRENT_COUNT = 0       
        #Open the text file containing the requested level
        with open(os.path.join('resources/levels', Level.__select_level(level))) as level:
            lines = level.readlines()
        #Loop through the level line by line
        for line in lines:
            line = line.rstrip()
            #Set x equal to the left border of the play area
            x = 21
            new_row = []
            #Remove the commas from the row and seperate into a list containing each brick
            line = line.split(',')
            #Loop through each brick in the line
            for brick in line:
                #if the brick is equal to 0, simply move the x value over 54 pixels and continue onto the next brick
                if brick == '00':
                    x += 54
                    continue
                #Append each brick object to the new_row list and then move the x variable over 54 pixels
                new_row.append(Brick(x, y, IMAGES[brick], BRICK_VALUES[brick]))
                x += 54
                #Add 1 to the current count of bricks in the level
                config.CURRENT_COUNT += 1
            #move the y variable down by 22 pixels
            y += 22
            #Append the new_row to the level
            Rows.append(new_row)
        

IMAGES = {  'BL' : config.BRICK_IMGS['brick_blue_img'],
            'GR' : config.BRICK_IMGS['brick_green_img'],
            'OR' : config.BRICK_IMGS['brick_orange_img'],
            'PI' : config.BRICK_IMGS['brick_pink_img'],
            'PU' : config.BRICK_IMGS['brick_purple_img'],
            'RE' : config.BRICK_IMGS['brick_red_img'],
            'YE' : config.BRICK_IMGS['brick_yellow_img'],
}
    
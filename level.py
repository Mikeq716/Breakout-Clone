import pygame
from config import *
from brick import Brick, BRICK_VALUES

class Level:
    current_level = 0

    #Function New Level
    #Function New Level adds 1 to the current level and then loads the new level
    def new_level(level, Rows):
        Level.current_level += 1
        Level.__load_level(50, Rows, Level.current_level)

    #Function Select Level
    #Function Select Level returns a string containing the name of the txt file containing the level to be opened
    def __select_level(level):
        return 'level' + str(level) + '.txt'

    #Function Load Level
    #Function Load Level loads the level from the text file containing it
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

    
    
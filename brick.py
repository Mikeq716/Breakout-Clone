import pygame
import random
from config import *
from scorecard import Scorecard
from powerup import *

class Brick:
    def __init__(self, x, y, img, value):
        self.__pos = pygame.math.Vector2(x,y)
        self.__img = img
        self.__value = value

    @property
    def get_pos(self):
        return pygame.math.Vector2(self.__pos.x, self.__pos.y)

    @property
    def get_value(self):
        return self.__value

    def update(self):
        SCREEN.blit(self.__img, [self.__pos.x, self.__pos.y])

    def hit(self, row, pu_list):
        if random.randint(1, 20) == 1:
            pu = random.randint(1, 3)
            pu_list.append(POWERUPS[pu](self.__pos.x, self.__pos.y, PU_IMG[pu]))
        row.remove(self)


BRICK_VALUES = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}        

        

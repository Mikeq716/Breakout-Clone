import pygame
import random

from .. import config

class Brick:
    def __init__(self, x, y, img, value):
        self.__pos = pygame.math.Vector2(x,y)
        self.__dir = pygame.math.Vector2(0.5, 0).normalize()
        self.__img = img
        self.__value = value
        self.speed = 0.5

    #Function Get Pos returns the bricks position
    @property
    def get_pos(self):
        return self.__pos

    #Function Get Value returns the bricks value
    @property
    def get_value(self):
        return self.__value

    #Function Draw draws the brick to the screen
    def draw(self, surface):
        #If the hidden powerup is not active, blit the brick to the screen
        if config.HIDE_BRICKS == False:
            surface.blit(self.__img, [self.__pos.x, self.__pos.y])


BRICK_VALUES = {'BL': 10, 'GR': 20, 'OR': 30, 'PI': 40, 'PU': 50, 'RE': 60, 'YE': 70}        

        

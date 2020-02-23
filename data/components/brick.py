import pygame
import random

from .. import config

class Brick:
    def __init__(self, x, y, img, value):
        self.__pos = pygame.math.Vector2(x,y)
        self.__dir = pygame.math.Vector2(0.5, 0).normalize()
        self.__img = img
        self.__value = value
        self.locked = False
        self.speed = 0.5

    #Function Get Pos
    #Function Get Pos returns the bricks position
    @property
    def get_pos(self):
        return self.__pos

    #Function Get Value
    #Function Get Value returns the bricks value
    @property
    def get_value(self):
        return self.__value

    #Function Draw
    #Function Draw draws the brick to the screen
    def draw(self, surface):
        if config.HIDE_BRICKS == False:
            surface.blit(self.__img, [self.__pos.x, self.__pos.y])


class Locked_Brick(Brick):
    def __init__(self, x, y, img, value):
        self.__pos = pygame.math.Vector2(x,y)
        self.__dir = pygame.math.Vector2(0.5, 0).normalize()
        self.__img = img
        self.__value = 0
        self.locked = True
        self.speed = 0.5   

    #Function Get Pos
    #Function Get Pos returns the bricks position
    @property
    def get_pos(self):
        return self.__pos

    #Function Get Value
    #Function Get Value returns the bricks value
    @property
    def get_value(self):
        return self.__value

    #Function Draw
    #Function Draw draws the brick to the screen
    def draw(self, surface):
        if config.HIDE_BRICKS == False:
            surface.blit(self.__img, [self.__pos.x, self.__pos.y])


BRICK_VALUES = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}        

        

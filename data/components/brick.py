import pygame
import random

from .. import config

class Brick:
    def __init__(self, x, y, img, value, locked, moving):
        self.__pos = pygame.math.Vector2(x,y)
        self.__dir = pygame.math.Vector2(0.5, 0).normalize()
        self.__img = img
        self.__value = value
        self.locked = locked
        self.moving = moving
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

    #Function Move
    #Function Move moves brick back and forth across the screen if self.moving is set to True
    def move(self, delta):
        if self.moving == True:
            if self.__pos.x + self.__dir.x * self.speed * delta <= 0:
                self.__dir.x *= -1
            if self.__pos.x + config.BRICK_WIDTH + self.__dir.x * self.speed * delta >= 800:
                self.__dir.x *= -1

    #Function Draw
    #Function Draw draws the brick to the screen
    def draw(self, surface):
        if config.HIDE_BRICKS == False:
            surface.blit(self.__img, [self.__pos.x, self.__pos.y])

BRICK_VALUES = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}        

        

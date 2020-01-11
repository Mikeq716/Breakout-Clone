import pygame
from config import *
from scorecard import Scorecard

class Brick:
    def __init__(self, x, y, img, value):
        self.x = x
        self.y = y
        self.img = img
        self.value = value

    def update(self):
        SCREEN.blit(self.img, [self.x, self.y])

    def hit(self, row):
        row.remove(self)

        
        

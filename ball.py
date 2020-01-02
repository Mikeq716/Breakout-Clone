import pygame
from config import *

#Ball class definition

class Ball:
    def __init__(self):
        self.position = pygame.math.Vector2(10, 10 )
        self.direction = pygame.math.Vector2(5, 1).normalize()

    def update(self):
        self.move()
        SCREEN.blit(ball_img, self.position)

    def move(self):
        self.position += self.direction * BALL_SPEED



        
        

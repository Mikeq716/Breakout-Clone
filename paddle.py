import pygame
from config import *

#Paddle class definition

class Paddle:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = PADDLE_Y

    def update(self, delta, ball):
        self.__move()
        SCREEN.blit(paddle_img, [self.x, self.y])

    def __move(self):
        paddle_move = pygame.mouse.get_rel()
        self.x += paddle_move[0] * 0.5
        if self.x < 0:
            self.x = 0
        elif self.x >= SCREEN_WIDTH - PADDLE_WIDTH :
            self.x = SCREEN_WIDTH - PADDLE_WIDTH
import pygame
from config import *

#Paddle class definition

class Paddle:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = PADDLE_Y
        self.speed = PADDLE_SPEED

    def update(self):
        self.move()
        SCREEN.blit(paddle_img, [self.x, self.y])

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x <= 0:
                self.x = 0
            else:
                self.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            if self.x >= SCREEN_WIDTH - PADDLE_WIDTH:
                self.x = SCREEN_WIDTH - PADDLE_WIDTH
            else:
                self.x += PADDLE_SPEED
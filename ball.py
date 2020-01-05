import pygame
from config import *

#Ball class definition

class Ball:
    def __init__(self):
        self.position = pygame.math.Vector2(10, 10 )
        self.direction = pygame.math.Vector2(1, 1).normalize()

    def update(self, delta):
        self.move(delta)
        SCREEN.blit(ball_img, self.position)

    def move(self, delta):
        if self.position.x + BALL_WIDTH + self.direction.x * BALL_SPEED * delta >= 800:
            self.direction.x *= -1
        if self.position.x + self.direction.x * BALL_SPEED * delta <= 0:
            self.direction.x *= -1
        if self.position.y + self.direction.y * BALL_SPEED * delta <= 0:
            self.direction.y *= -1
        if self.position.y + self.direction.y * BALL_SPEED * delta >= 600:
            self.direction.y *= -1

        self.position += self.direction * BALL_SPEED * delta



        
        

import pygame
from config import *

class Brick:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def update(self, ball, delta):
        self.check_collision(ball, delta)
        SCREEN.blit(self.img, [self.x, self.y])

    def check_collision(self, ball, delta):
        check_x_pos = ball.position.x + (BALL_WIDTH / 2) + ball.direction.x * BALL_SPEED * delta

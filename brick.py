import pygame
from config import *
from scorecard import Scorecard

class Brick:
    def __init__(self, x, y, img, value):
        self.x = x
        self.y = y
        self.img = img
        self.hit = False
        self.value = value

    def update(self, ball, delta):
        self._check_collision(ball, delta)
        SCREEN.blit(self.img, [self.x, self.y])

    def _check_collision(self, ball, delta):
        check_x = ball.position.x
        check_y = ball.position.y
        if check_x >= self.x and check_x <= self.x + BRICK_WIDTH: 
            if check_y <= self.y + BRICK_HEIGHT and check_y >= self.y + BRICK_HEIGHT - (BALL_SPEED * delta) and ball.direction.y < 0:
                self.hit = True
                ball.direction.y *= -1
                Scorecard.current_score += self.value
        if check_x >= self.x and check_x <= self.x + BRICK_WIDTH:
            if check_y >= self.y and check_y <= self.y + (BALL_SPEED * delta) and ball.direction.y > 0:
                self.hit = True
                ball.direction.y *= -1
                Scorecard.current_score += self.value
        if check_y >= self.y and check_y <= self.y + BRICK_HEIGHT:
            if check_x >= self.x and check_x <= self.x + (BALL_SPEED * delta) and ball.direction.x > 0:
                self.hit = True
                ball.direction.x *= -1
                Scorecard.current_score += self.value
        if check_y >= self.y and check_y <= self.y + BRICK_HEIGHT:
            if check_x <= self.x + BRICK_WIDTH and check_x >= self.x + BRICK_WIDTH - (BALL_SPEED * delta) and ball.direction.x < 0:
                self.hit = True
                ball.direction.x *= -1
                Scorecard.current_score += self.value

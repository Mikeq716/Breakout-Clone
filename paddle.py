import pygame
from config import *

#Paddle class definition

class Paddle:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = PADDLE_Y
        self.speed = PADDLE_SPEED

    def update(self, delta, ball):
        self.move(delta)
        self.check_collision(ball, delta)
        SCREEN.blit(paddle_img, [self.x, self.y])

    def move(self, delta):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x <= 0:
                self.x = 0
            else:
                self.x -= PADDLE_SPEED * delta
        if keys[pygame.K_RIGHT]:
            if self.x >= SCREEN_WIDTH - PADDLE_WIDTH:
                self.x = SCREEN_WIDTH - PADDLE_WIDTH
            else:
                self.x += PADDLE_SPEED * delta

    def check_collision(self, ball, delta):
        if ball.position.y + BALL_HEIGHT + ball.direction.y * BALL_SPEED * delta >= PADDLE_Y:
            if ball.position.x + BALL_WIDTH + ball.direction.x * BALL_SPEED * delta > self.x and ball.position.x + ball.direction.x * BALL_SPEED * delta < self.x + PADDLE_WIDTH:
                ball.direction.y *= -1

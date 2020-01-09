import pygame
from config import *

#Ball class definition

class Ball:
    def __init__(self, paddle):
        self.start = False
        self.position = pygame.math.Vector2(paddle.x + PADDLE_WIDTH/2 + BALL_WIDTH / 2)
        self.direction = pygame.math.Vector2(0, -1).normalize()

    def update(self, delta, paddle):
        self.__move(delta)
        SCREEN.blit(ball_img, self.position)

    def ball_active(self, paddle, ball_active, delta):
        if ball_active == False:
            self.position.x = paddle.x + PADDLE_WIDTH / 2 - BALL_WIDTH / 2
            self.position.y = PADDLE_Y - BALL_HEIGHT - 1
        else:
            if self.position.y > PADDLE_Y - BALL_HEIGHT + (BALL_SPEED * delta):
                ball_active = False
        return ball_active

    def __move(self, delta):        
        if self.position.x + BALL_WIDTH + self.direction.x * BALL_SPEED * delta >= SCREEN_WIDTH:
            self.direction.x *= -1
        if self.position.x + self.direction.x * BALL_SPEED * delta <= 0:
            self.direction.x *= -1
        if self.position.y + self.direction.y * BALL_SPEED * delta <= 35:
            self.direction.y *= -1            
        self.position += self.direction * BALL_SPEED * delta
        
        

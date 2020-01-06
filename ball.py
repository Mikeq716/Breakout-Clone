import pygame
from config import *

#Ball class definition

class Ball:
    def __init__(self, paddle):
        self.start = False
        self.position = pygame.math.Vector2(paddle.x + PADDLE_WIDTH/2 + BALL_WIDTH / 2)
        self.direction = pygame.math.Vector2(0, -1).normalize()

    def update(self, delta, paddle, fresh_ball):
        self.fresh_ball(fresh_ball, paddle)
        self.move(delta, fresh_ball)
        SCREEN.blit(ball_img, self.position)

    def move(self, delta, fresh_ball):        
        if self.position.x + BALL_WIDTH + self.direction.x * BALL_SPEED * delta >= SCREEN_WIDTH:
            self.direction.x *= -1
        if self.position.x + self.direction.x * BALL_SPEED * delta <= 0:
            self.direction.x *= -1
        if self.position.y + self.direction.y * BALL_SPEED * delta <= 0:
            self.direction.y *= -1            
        self.position += self.direction * BALL_SPEED * delta

    def fresh_ball(self, fresh_ball, paddle):
        if fresh_ball == True:
            self.position.y = PADDLE_Y - BALL_HEIGHT + 1
            self.position.x = paddle.x + (PADDLE_WIDTH / 2) - (BALL_WIDTH / 2)


        
        

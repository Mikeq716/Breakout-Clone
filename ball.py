import pygame
from config import *

#Ball class definition

class Ball:
    def __init__(self):
        self.position = pygame.math.Vector2(0, 0 )
        self.direction = pygame.math.Vector2(1, 1).normalize()

    def update(self, delta, paddle):
        self.move(delta, paddle)
        self.check_paddle_collisions(paddle)
        self.position += self.direction * BALL_SPEED * delta
        SCREEN.blit(ball_img, self.position)

    def move(self, delta, paddle):
        if self.position.x <= 1:
            self.direction.x *= -1
        if self.position.x >= 799 - BALL_WIDTH:
            self.direction.x *= -1
        if self.position.y < 1:
            self.direction.y *= -1
        
    def check_paddle_collisions(self, paddle):
        if self.position.y + BALL_HEIGHT >= PADDLE_Y - 1:
            if self.position.x >= paddle.x and self.position.x <= paddle.x + PADDLE_WIDTH:
                self.direction.y *= -1
 



        
        

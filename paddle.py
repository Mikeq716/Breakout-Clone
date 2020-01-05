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
        check_pos_x = ball.position.x + (BALL_WIDTH / 2) + ball.direction.x * BALL_SPEED * delta
        check_pos_y = ball.position.y + BALL_HEIGHT + ball.direction.y * BALL_SPEED * delta
        paddle_split_pos = self.x + (PADDLE_WIDTH / 2) + PADDLE_SPEED * delta
        y_vel = ball.direction.y
        if check_pos_y >= PADDLE_Y:
            if check_pos_x >= self.x and check_pos_x <= self.x + PADDLE_WIDTH:
                if check_pos_x < paddle_split_pos:
                    ball_dist = paddle_split_pos - check_pos_x
                    x_vel = (ball_dist / (PADDLE_WIDTH / 2)) * -1
                    ball.direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()
                if check_pos_x > paddle_split_pos:
                    ball_dist = check_pos_x - paddle_split_pos
                    x_vel = ball_dist / (PADDLE_WIDTH / 2)
                    ball.direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()
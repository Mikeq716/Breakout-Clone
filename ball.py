import pygame
from config import *
from scorecard import Scorecard

#Ball class definition

class Ball:
    def __init__(self, paddle):
        self.start = False
        self.position = pygame.math.Vector2(paddle.x + PADDLE_WIDTH/2 + BALL_WIDTH / 2)
        self.direction = pygame.math.Vector2(0, -1).normalize()
        self.ball_active = False

    def update(self, ball, paddle, delta):
        self.__move(delta)
        self.__check_paddle_collision(paddle, delta)
        self.is_ball_active(paddle, delta)
        SCREEN.blit(ball_img, self.position)

    def reset_ball(self):
        self.ball_active = False
        self.direction.x = 0
        self.direction.y = 1

    def is_ball_active(self, paddle, delta):
        if self.ball_active == False:
            self.position.x = paddle.x + PADDLE_WIDTH / 2 - BALL_WIDTH / 2
            self.position.y = PADDLE_Y - BALL_HEIGHT - 1
        else:
            if self.position.y > PADDLE_Y - BALL_HEIGHT + (BALL_SPEED * delta):
                self.reset_ball()
                Scorecard.lives_left += -1

    def check_brick_collision(self, ball, brick, delta):
        check_x = self.position.x
        check_y = self.position.y
        if check_x >= brick.x and check_x <= brick.x + BRICK_WIDTH: 
            if check_y <= brick.y + BRICK_HEIGHT and check_y >= brick.y + BRICK_HEIGHT - (BALL_SPEED * delta) and self.direction.y < 0:
                self.direction.y *= -1
                return True
        if check_x >= brick.x and check_x <= brick.x + BRICK_WIDTH:
            if check_y >= brick.y and check_y <= brick.y + (BALL_SPEED * delta) and self.direction.y > 0:
                self.direction.y *= -1
                return True
        if check_y >= brick.y and check_y <= brick.y + BRICK_HEIGHT:
            if check_x >= brick.x and check_x <= brick.x + (BALL_SPEED * delta) and self.direction.x > 0:
                self.direction.x *= -1
                return True
        if check_y >= brick.y and check_y <= brick.y + BRICK_HEIGHT:
            if check_x <= brick.x + BRICK_WIDTH and check_x >= brick.x + BRICK_WIDTH - (BALL_SPEED * delta) and self.direction.x < 0:
                self.direction.x *= -1
                return True

    def __check_paddle_collision(self, paddle, delta):
        check_pos_x = self.position.x + (BALL_WIDTH / 2) + self.direction.x * BALL_SPEED * delta
        check_pos_y = self.position.y + BALL_HEIGHT + self.direction.y * BALL_SPEED * delta
        paddle_split_pos = paddle.x + (PADDLE_WIDTH / 2)
        y_vel = self.direction.y
        if check_pos_y >= PADDLE_Y:
            if check_pos_x >= paddle.x and check_pos_x <= paddle.x + PADDLE_WIDTH:
                if check_pos_x < paddle_split_pos:
                    ball_dist = paddle_split_pos - check_pos_x
                    x_vel = ball_dist / (PADDLE_WIDTH / 2) * -1
                    self.direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()
                if check_pos_x > paddle_split_pos:
                    ball_dist = check_pos_x - paddle_split_pos
                    x_vel = ball_dist / (PADDLE_WIDTH / 2)
                    self.direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()

    def __move(self, delta):        
        if self.position.x + BALL_WIDTH + self.direction.x * BALL_SPEED * delta >= SCREEN_WIDTH:
            self.direction.x *= -1
        if self.position.x + self.direction.x * BALL_SPEED * delta <= 0:
            self.direction.x *= -1
        if self.position.y + self.direction.y * BALL_SPEED * delta <= 35:
            self.direction.y *= -1            
        self.position += self.direction * BALL_SPEED * delta
        
        

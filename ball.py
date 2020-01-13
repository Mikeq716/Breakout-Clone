import pygame
from config import *
from paddle import Paddle
from brick import Brick
from scorecard import Scorecard

#Ball class definition
class Ball:
    def __init__(self, paddle):
        self.start = False
        self.position = pygame.math.Vector2(paddle.get_pos + paddle.get_width / 2 + BALL_WIDTH / 2)
        self.direction = pygame.math.Vector2(0, -1).normalize()
        self.ball_active = False
        self.__ball_speed = 0.5

    def update(self, ball, paddle, delta):
        self.__move(delta)
        self.__check_paddle_collision(paddle, delta)
        self.is_ball_active(paddle, delta)
        SCREEN.blit(ball_img, self.position)

    def reset_ball(self, paddle):
        paddle_pos = paddle.get_pos
        paddle_width = paddle.get_width
        self.ball_active = False
        self.direction.x = 0
        self.direction.y = 1
        self.position.x = paddle_pos + paddle_width / 2 - BALL_WIDTH / 2
        self.position.y = PADDLE_Y - BALL_HEIGHT - 1
        self.decrease_speed()

    def increase_speed(self):
        self.__ball_speed += 0.10

    def decrease_speed(self):
        self.__ball_speed -+ 0.10

    def is_ball_active(self, paddle, delta):
        paddle_pos = paddle.get_pos
        paddle_width = paddle.get_width
        if self.ball_active == False:
            self.position.x = paddle_pos + paddle_width / 2 - BALL_WIDTH / 2
            self.position.y = PADDLE_Y - BALL_HEIGHT - 1
        else:
            if self.position.y > PADDLE_Y - BALL_HEIGHT + (self.__ball_speed * delta):
                self.reset_ball(paddle)
                Scorecard.lives_left += -1

    def check_brick_collision(self, ball, brick, delta):
        check_x = self.position.x
        check_y = self.position.y
        brick_pos = brick.get_pos
        if check_x >= brick_pos.x and check_x <= brick_pos.x + BRICK_WIDTH: 
            if check_y <= brick_pos.y + BRICK_HEIGHT and check_y >= brick_pos.y + BRICK_HEIGHT - (self.__ball_speed * delta) and self.direction.y < 0:
                self.direction.y *= -1
                return True
        if check_x >= brick_pos.x and check_x <= brick_pos.x + BRICK_WIDTH:
            if check_y >= brick_pos.y and check_y <= brick_pos.y + (self.__ball_speed * delta) and self.direction.y > 0:
                self.direction.y *= -1
                return True
        if check_y >= brick_pos.y and check_y <= brick_pos.y + BRICK_HEIGHT:
            if check_x >= brick_pos.x and check_x <= brick_pos.x + (self.__ball_speed * delta) and self.direction.x > 0:
                self.direction.x *= -1
                return True
        if check_y >= brick_pos.y and check_y <= brick_pos.y + BRICK_HEIGHT:
            if check_x <= brick_pos.x + BRICK_WIDTH and check_x >= brick_pos.x + BRICK_WIDTH - (self.__ball_speed * delta) and self.direction.x < 0:
                self.direction.x *= -1
                return True

    def __check_paddle_collision(self, paddle, delta):
        paddle_pos = paddle.get_pos
        paddle_width = paddle.get_width
        check_pos_x = self.position.x + (BALL_WIDTH / 2) + self.direction.x * self.__ball_speed * delta
        check_pos_y = self.position.y + BALL_HEIGHT + self.direction.y * self.__ball_speed * delta
        paddle_split_pos = paddle_pos + (paddle_width / 2)
        y_vel = self.direction.y
        if check_pos_y >= PADDLE_Y:
            if check_pos_x >= paddle_pos and check_pos_x <= paddle_pos + paddle_width:
                if check_pos_x < paddle_split_pos:
                    ball_dist = paddle_split_pos - check_pos_x
                    x_vel = ball_dist / (paddle_width / 2) * -1
                    self.direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()
                if check_pos_x > paddle_split_pos:
                    ball_dist = check_pos_x - paddle_split_pos
                    x_vel = ball_dist / (paddle_width / 2)
                    self.direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()

    def __move(self, delta):        
        if self.position.x + BALL_WIDTH + self.direction.x * self.__ball_speed * delta >= SCREEN_WIDTH:
            self.direction.x *= -1
        if self.position.x + self.direction.x * self.__ball_speed * delta <= 0:
            self.direction.x *= -1
        if self.position.y + self.direction.y * self.__ball_speed * delta <= 35:
            self.direction.y *= -1            
        self.position += self.direction * self.__ball_speed * delta
        
        

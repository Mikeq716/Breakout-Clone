import pygame
from config import *
from paddle import Paddle
from brick import Brick
from scorecard import Scorecard

#Ball class definition
class Ball:
    def __init__(self, paddle):
        self.__position = pygame.math.Vector2(paddle.get_pos + paddle.get_width / 2 + BALL_WIDTH / 2)
        self.__direction = pygame.math.Vector2(0, -1).normalize()
        self.__ball_active = False
        self.__ball_speed = 0.6

    #Update Function
    #Update function calculates new position and draws ball, checks for paddle collision and checks if ball is active
    def update(self, ball, paddle, delta):
        self.__move(delta)
        self.__check_paddle_collision(paddle, delta)
        self.is_ball_active(paddle, delta)
        SCREEN.blit(ball_img, self.__position)

    #Activate Ball Function
    #Activate Ball Function sets the balls __ball_active variable to True
    def activate_ball(self):
        self.__ball_active = True

    #Reset Ball Funtion
    #Reset Ball Function resets the ball to the middle of the paddle, and resets its direction vector to straight up
    def reset_ball(self, paddle):
        paddle_pos = paddle.get_pos
        paddle_width = paddle.get_width
        self.__ball_active = False
        self.__direction.x = 0
        self.__direction.y = 1
        self.__position.x = paddle_pos + paddle_width / 2 - BALL_WIDTH / 2
        self.__position.y = PADDLE_Y - BALL_HEIGHT - 1

    #Increase Speed Function
    #Increase Speed Function increases the balls __ball_speed variable by 0.10
    def increase_speed(self):
        self.__ball_speed += 0.10

    #Decrease Speed Function
    #Decrease Speed Function decreases the balls __ball_speed variable by 0.10
    def decrease_speed(self):
        self.__ball_speed -= 0.10

    #Is Ball Active Function
    #Is Ball Active Function moves ball to middle of paddle each frame if __ball_active variable is False
    #Is Ball Active Function sets __ball_active to False and calls reset_ball and decrease_speed and removes a life if ball is active and moves below the paddle
    def is_ball_active(self, paddle, delta):
        paddle_pos = paddle.get_pos
        paddle_width = paddle.get_width
        if self.__ball_active == False:
            self.__position.x = paddle_pos + paddle_width / 2 - BALL_WIDTH / 2
            self.__position.y = PADDLE_Y - BALL_HEIGHT - 1
        else:
            if self.__position.y > PADDLE_Y - BALL_HEIGHT + (self.__ball_speed * delta):
                self.reset_ball(paddle)
                self.decrease_speed()
                Scorecard.lives_left += -1

    #Check Brick Collision Function
    #Check Brick Collision Function checks if ball has collided with brick and if it has it reverses balls direction on the correct axis and returns true
    def check_brick_collision(self, ball, brick, delta):
        check_x = self.__position.x
        check_y = self.__position.y
        brick_pos = brick.get_pos
        if check_x >= brick_pos.x and check_x <= brick_pos.x + BRICK_WIDTH: 
            if check_y <= brick_pos.y + BRICK_HEIGHT and check_y >= brick_pos.y + BRICK_HEIGHT - (self.__ball_speed * delta) and self.__direction.y < 0:
                self.__direction.y *= -1
                return True
        if check_x >= brick_pos.x and check_x <= brick_pos.x + BRICK_WIDTH:
            if check_y >= brick_pos.y and check_y <= brick_pos.y + (self.__ball_speed * delta) and self.__direction.y > 0:
                self.__direction.y *= -1
                return True
        if check_y >= brick_pos.y and check_y <= brick_pos.y + BRICK_HEIGHT:
            if check_x >= brick_pos.x and check_x <= brick_pos.x + (self.__ball_speed * delta) and self.__direction.x > 0:
                self.__direction.x *= -1
                return True
        if check_y >= brick_pos.y and check_y <= brick_pos.y + BRICK_HEIGHT:
            if check_x <= brick_pos.x + BRICK_WIDTH and check_x >= brick_pos.x + BRICK_WIDTH - (self.__ball_speed * delta) and self.__direction.x < 0:
                self.__direction.x *= -1
                return True

    #Check Paddle Collision Function
    #Check Paddle Collision Function checks if ball has collided with the paddle and returns true if it has
    #Check Paddle Collision Function calculates and sets the balls correct bounce angle depending on where on the paddle the collision happened
    def __check_paddle_collision(self, paddle, delta):
        paddle_pos = paddle.get_pos
        paddle_width = paddle.get_width
        check_pos_x = self.__position.x + (BALL_WIDTH / 2) + self.__direction.x * self.__ball_speed * delta
        check_pos_y = self.__position.y + BALL_HEIGHT + self.__direction.y * self.__ball_speed * delta
        paddle_split_pos = paddle_pos + (paddle_width / 2)
        y_vel = self.__direction.y
        if check_pos_y >= PADDLE_Y:
            if check_pos_x >= paddle_pos and check_pos_x <= paddle_pos + paddle_width:
                if check_pos_x < paddle_split_pos:
                    ball_dist = paddle_split_pos - check_pos_x
                    x_vel = ball_dist / (paddle_width / 2) * -1
                    self.__direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()
                if check_pos_x > paddle_split_pos:
                    ball_dist = check_pos_x - paddle_split_pos
                    x_vel = ball_dist / (paddle_width / 2)
                    self.__direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()

    #Function Move
    #Function Move reverses the balls direction if it hits a wall and calculates the balls movement for the current frame
    def __move(self, delta):        
        if self.__position.x + BALL_WIDTH + self.__direction.x * self.__ball_speed * delta >= SCREEN_WIDTH:
            self.__direction.x *= -1
        if self.__position.x + self.__direction.x * self.__ball_speed * delta <= 0:
            self.__direction.x *= -1
        if self.__position.y + self.__direction.y * self.__ball_speed * delta <= 35:
            self.__direction.y *= -1            
        self.__position += self.__direction * self.__ball_speed * delta
        
        

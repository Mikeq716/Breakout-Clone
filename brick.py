import pygame
from config import *

class Brick:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.hit = False

    def update(self, ball, delta):
        self.check_collision(ball, delta)
        SCREEN.blit(self.img, [self.x, self.y])

    def check_collision(self, ball, delta):
        check_x_pos = ball.position.x
        check_y_pos = ball.position.y
        
        if check_x_pos > self.x or check_x_pos < self.x + BRICK_WIDTH or check_y_pos > self.y or check_y_pos < self.y + BRICK_HEIGHT:
            if check_x_pos > self.x and check_x_pos < self.x + BRICK_WIDTH and check_y_pos < self.y + BRICK_HEIGHT and ball.direction.y < 0:
                self.hit = True
                ball.direction.y *= -1
            elif check_x_pos > self.x and check_x_pos < self.x + BRICK_WIDTH and check_y_pos > self.y and check_y_pos < self.y + BRICK_HEIGHT and ball.direction.y > 0:
                self.hit = True
                ball.direction.y *= -1
            elif check_y_pos > self.y and check_y_pos < self.y + BRICK_HEIGHT and check_x_pos > self.x and check_x_pos < self.x + 5 and ball.direction.x > 0:
                self.hit = True
                ball.direction.x *= -1
            elif check_y_pos > self.y and check_y_pos < self.y + BRICK_HEIGHT and check_x_pos < self.x + BRICK_WIDTH and check_x_pos > self.x + BRICK_WIDTH - 5 and ball.direction.x < 0:
                self.hit = True
                ball.direction.x *= -1 
            elif check_x_pos > self.x and check_x_pos < self.x + 5 and check_y_pos < self.y + BRICK_HEIGHT and check_y_pos > self.y + BRICK_HEIGHT - 5 and ball.direction.x > 0 and ball.direction.y < 0:
                self.hit = True
                ball.direction.y *= -1
            elif check_x_pos < self.x + BRICK_WIDTH - 5 and check_y_pos > self.y + BRICK_HEIGHT and check_y_pos < self.y + BRICK_HEIGHT - 5 and ball.direction.x < 0 and ball.direction.y < 0:
                self.hit = True
                ball.direction.y *= -1
            elif check_x_pos < self.x + BRICK_WIDTH and check_x_pos > self.x + BRICK_WIDTH - 5 and check_y_pos > self.y and check_y_pos < self.y + 5 and ball.direction.x < 0 and ball.direction.y > 0:
                self.hit = True
                ball.direction.y *= -1
            elif check_x_pos > self.x and check_x_pos < self.x + 5 and check_y_pos > self.y and check_y_pos < self.y + 5 and ball.direction.x > 0 and ball.direction.y > 0:
                self.hit = True
                ball.direction.y *= -1
                


                
    def create_row(list, y, image):
        x = BRICK_WIDTH
        for i in range(16):
            list.append(Brick(x, y, image))
            x += BRICK_WIDTH

    def update_list(brick_list, ball, delta):
        for obj in brick_list:
            obj.update(ball, delta)
            if obj.hit == True:
                ball.direction.y *= 1
                brick_list.remove(obj)
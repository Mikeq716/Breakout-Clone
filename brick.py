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
        check_x_pos = ball.position.x + (BALL_WIDTH / 2) + ball.direction.x * BALL_SPEED * delta
        check_y_pos = ball.position.y + (BALL_HEIGHT / 2) + ball.direction.y * BALL_SPEED * delta

        if check_x_pos >= self.x and check_x_pos <= self.x + BRICK_WIDTH and check_y_pos >= self.y and check_y_pos <= self.y + BRICK_HEIGHT:
            self.hit = True
            ball.direction.y *= -1

    def create_row(list, y, image):
        x = 54
        for i in range(16):
            list.append(Brick(x, y, image))
            x += 54

    def update_list(brick_list, ball, delta):
        for obj in brick_list:
            obj.update(ball, delta)
            if obj.hit == True:
                ball.direction.y *= 1
                brick_list.remove(obj)
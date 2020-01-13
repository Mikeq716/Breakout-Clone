import pygame
import random
from config import *
from scorecard import Scorecard

class Powerup:
    def __init__(self, x, y, img):
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(random.randint(-1, 1), 1).normalize()
        self.img = img

    def update(self, delta, paddle, pu_list):
        self.move(delta)
        self.check_activated(paddle, pu_list)
        if self.position.y > PADDLE_Y:
            self.delete(pu_list)
        SCREEN.blit(self.img, self.position)

    def move(self, delta):
        self.position += self.velocity * delta * 0.25
        if self.position.x <= 0:
            self.velocity.x *= -1
        elif self.position.x + powerup_health_img.get_width() >= SCREEN_WIDTH:
            self.velocity.x *= -1

    def check_activated(self, paddle, pu_list):
        paddle_pos = paddle.get_pos
        paddle_width = paddle.get_width
        if self.position.y + powerup_health_img.get_height() >= PADDLE_Y and self.position.y <= PADDLE_Y:
            if self.position.x >= paddle_pos and self.position.x + powerup_health_img.get_width() <= paddle_pos + paddle_width:
                self.activate(pu_list, paddle)

    def delete(self, pu_list):
        pu_list.remove(self)


class HealthPowerup(Powerup):
    def activate(self, pu_list, paddle):
        Scorecard.add_life()
        self.delete(pu_list)


class IncreasePaddleSize(Powerup):
    def activate(self, pu_list, paddle):
        paddle.increase_paddle_size()
        self.delete(pu_list)


class DecreasePaddleSize(Powerup):
    def activate(self, pu_list, paddle):
        paddle.decrease_paddle_size()
        self.delete(pu_list)

   
POWERUPS = {1: HealthPowerup, 2: IncreasePaddleSize, 3: DecreasePaddleSize}
PU_IMG = {1: powerup_health_img, 2: powerup_increase_paddle_img, 3: powerup_decrease_paddle_img}

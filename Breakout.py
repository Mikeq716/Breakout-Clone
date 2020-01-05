import pygame
import os
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick


def main():
    #Initiate and set up pygame
    pygame.init()
    pygame.display.set_caption("Breakout")

    #Create game objects
    Clock = pygame.time.Clock()
    paddle = Paddle()
    ball = Ball(paddle)
    red_row, yellow_row, blue_row, green_row, purple_row, pink_row, orange_row = [], [], [], [], [], [], []

    Brick.create_row(red_row, 10, brick_red_img)
    Brick.create_row(yellow_row, 32, brick_yellow_img)
    Brick.create_row(blue_row, 54, brick_blue_img)
    Brick.create_row(green_row, 76, brick_green_img)
    Brick.create_row(purple_row, 98, brick_purple_img)
    Brick.create_row(pink_row, 120, brick_pink_img)
    Brick.create_row(orange_row, 142, brick_orange_img)

    #Main game loop
    Run = True
    while Run:
        delta = Clock.tick_busy_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        SCREEN.fill((0, 0, 0))

        Brick.update_list(red_row, ball, delta)
        Brick.update_list(yellow_row, ball, delta)
        Brick.update_list(blue_row, ball, delta)
        Brick.update_list(green_row, ball, delta)
        Brick.update_list(purple_row, ball, delta)
        Brick.update_list(pink_row, ball, delta)
        Brick.update_list(orange_row, ball, delta)

        paddle.update(delta, ball)
        ball.update(delta)

        pygame.display.update()


if __name__ == '__main__':
    main()

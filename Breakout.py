import pygame
import os
from config import *
from paddle import Paddle
from ball import Ball


def main():
    #Initiate and set up pygame
    pygame.init()
    pygame.display.set_caption("Breakout")

    #Create game objects
    Clock = pygame.time.Clock()
    paddle = Paddle()
    ball = Ball()

    #Main game loop
    Run = True
    while Run:
        delta = Clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        SCREEN.fill((0, 0, 0))

        ball.update(delta, paddle)
        paddle.update(delta)

        pygame.display.update()


if __name__ == '__main__':
    main()

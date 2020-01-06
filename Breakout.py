import pygame
import os
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from game import Game


def main():
    #Initiate and set up pygame
    pygame.init()
    pygame.display.set_caption("Breakout")
    pygame.mouse.set_visible(0)

    #Create game objects
    paddle = Paddle()
    ball = Ball(paddle)
    game = Game()

    #Main game loop
    game.game_loop(paddle, ball)


if __name__ == '__main__':
    main()

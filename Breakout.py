import pygame
import os
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from game import Game


def main():
    #Create game objects
    game = Game()
    paddle = Paddle()
    ball = Ball(paddle)
    
    #Initiate pygame
    game.game_init()

    #Main game loop
    game.game_loop(paddle, ball)


if __name__ == '__main__':
    main()

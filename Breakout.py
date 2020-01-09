import pygame
from config import *
from game import Game
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard

def main():
    game = Game()
    paddle = Paddle()
    ball = Ball(paddle)

    #Initiate pygame
    game.game_init()

    #Main game loop
    game.game_loop(paddle, ball)


if __name__ == '__main__':
    main()

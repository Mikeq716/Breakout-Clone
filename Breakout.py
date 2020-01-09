import pygame
from config import *
from game import Game
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard

def main():
    game = Game()

    #Initiate pygame
    game.game_init()

    #Main game loop
    game.game_loop()


if __name__ == '__main__':
    main()

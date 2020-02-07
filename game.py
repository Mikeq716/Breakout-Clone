import pygame
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick, BRICK_VALUES
from level import Level
from scorecard import Scorecard
from gamehelper import Gamehelper
from powerup import Powerup, POWERUPS

class Game:
    def __init__(self):
        Level.current_level = 0
        Scorecard.current_score = 0
        Scorecard.lives_left = 3
    
    #game_loop contains the actual game loop
    def run_game(self, dt):
        

        for powerup in self.powerups:
            powerup.update(dt, self.paddle, self.powerups)
        
        if Scorecard.lives_left == 1:
            self.paddle.increase_paddle_size()
        
        if Scorecard.lives_left == 0:
            Gamehelper.game_over(self.rows, self.paddle, self.ball)

        Gamehelper.update_scorecard()
import pygame
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from level import Level
from scorecard import Scorecard
from powerup import Powerup

class Gamehelper:
    #Function Update Scorecard
    #Function Update Scorecard updates the scorecard to current values for the current frame
    def update_scorecard():
        Scorecard.draw_score(Scorecard.current_score)
        Scorecard.draw_level(Level.current_level)
        Scorecard.draw_lives(Scorecard.lives_left)

    #Function Game Over
    #Function Game over clears the level, resets the level to 1, resets lives to 3, resets the paddle size to normal, and loads the beginning level
    def game_over(Rows, paddle, ball):
            Rows.clear()
            Level.current_level = 0
            Scorecard.lives_left = 3
            paddle.reset_paddle_size()
            Gamehelper.load_level(Rows, ball)

    #Function Load Level
    #Function Load Level loads a new level and increases the ball speed by 0.10
    def load_level(Rows, ball):
        Level.new_level(Level.current_level, Rows)
        ball.increase_speed()
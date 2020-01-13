import pygame
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from level import Level
from scorecard import Scorecard
from powerup import Powerup

class Gamehelper:
    def update_scorecard():
        Scorecard.draw_score(Scorecard.current_score)
        Scorecard.draw_level(Level.current_level)
        Scorecard.draw_lives(Scorecard.lives_left)

    def game_over(Rows, paddle, ball):
            Rows.clear()
            Level.current_level = 0
            Scorecard.lives_left = 3
            paddle.reset_paddle_size()
            Gamehelper.load_level(Rows, ball)

    def load_level(Rows, ball):
        Level.new_level(Level.current_level, Rows)
        ball.increase_speed()
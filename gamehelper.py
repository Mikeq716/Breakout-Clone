import pygame
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from level import Level
from scorecard import Scorecard

class Gamehelper:
    def update_scorecard():
        Scorecard.draw_score(Scorecard.current_score)
        Scorecard.draw_level(Level.current_level)
        Scorecard.draw_lives(Scorecard.lives_left)

    def update_game_loop(ball, paddle, delta, Rows):
        SCREEN.fill((0, 0, 0))
        if len(Rows) == 0:
            ball.reset_ball()
            Gamehelper.load_level(Rows)
        ball.update(ball, paddle, delta)
        paddle.update(delta, ball)
        for row in Rows:
            if len(row) == 0:
                Rows.remove(row)
            for brick in row:
                brick.update()
                if ball.check_brick_collision(ball, brick, delta) == True:
                    Scorecard.add_score(brick.value)
                    brick.hit(row)
        if Scorecard.lives_left == 0:
            Gamehelper.game_over(Rows)

    def game_over(Rows):
            Rows.clear()
            Level.current_level = 0
            Scorecard.lives_left = 3   
            Gamehelper.load_level(Rows)

    def load_level(Rows):
        Level.new_level(Level.current_level, Rows)

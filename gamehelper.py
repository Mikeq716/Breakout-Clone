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
            Gamehelper.load_level(Rows)
        
        ball.update(ball, paddle, delta)
        paddle.update(delta, ball)

        for row in Rows:
            if len(row) == 0:
                Rows.remove(row)
            for brick in row:
                brick.update()
                if ball.check_brick_collision(ball, brick, delta) == True:
                    brick.hit(row)


    def load_level(Rows):
        Level.new_level(Level.current_level, Rows)

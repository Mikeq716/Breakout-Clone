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
    #Initiate game wide variables in __init__
    def __init__(self):
        self.Rows = []
        self.powerups = []

    #game_loop contains the actual game loop
    def game_loop(self, dt, ball, paddle):
        SCREEN.fill((0, 0, 0))
                    
        if len(self.Rows) == 0:
            ball.reset_ball(paddle)
            Gamehelper.load_level(self.Rows, ball)
            self.powerups.clear()
            paddle.reset_paddle_size()

        ball.update(ball, paddle, dt)
        paddle.update(dt, ball)
        
        for row in self.Rows:
            if len(row) == 0:
                self.Rows.remove(row)
            for brick in row:
                brick.update()
                if ball.check_brick_collision(ball, brick, dt) == True:
                    Scorecard.add_score(brick.get_value)
                    brick.hit(row, self.powerups)

        for powerup in self.powerups:
            powerup.update(dt, paddle, self.powerups)
        
        if Scorecard.lives_left == 1:
            self.paddle.increase_paddle_size()
        
        if Scorecard.lives_left == 0:
            Gamehelper.game_over(self.Rows, paddle, ball)

        Gamehelper.update_scorecard()
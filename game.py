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
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)
        self.rows = []
        self.powerups = []
        Level.current_level = 0
        Scorecard.current_score = 0
        Scorecard.lives_left = 3
    
    #game_loop contains the actual game loop
    def run_game(self, dt):
        SCREEN.fill((0, 0, 0))
                    
        if len(self.rows) == 0:
            self.ball.reset_ball(self.paddle)
            Gamehelper.load_level(self.rows, self.ball)
            self.powerups.clear()
            self.paddle.reset_paddle_size()

        self.ball.update(self.ball, self.paddle, dt)
        self.paddle.update(dt, self.ball)
        
        for row in self.rows:
            if len(row) == 0:
                self.rows.remove(row)
            for brick in row:
                brick.update()
                if self.ball.check_brick_collision(self.ball, brick, dt) == True:
                    Scorecard.add_score(brick.get_value)
                    brick.hit(row, self.powerups)

        for powerup in self.powerups:
            powerup.update(dt, self.paddle, self.powerups)
        
        if Scorecard.lives_left == 1:
            self.paddle.increase_paddle_size()
        
        if Scorecard.lives_left == 0:
            Gamehelper.game_over(self.rows, self.paddle, self.ball)

        Gamehelper.update_scorecard()
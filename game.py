import pygame
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from level import Level
from scorecard import Scorecard
from gamehelper import Gamehelper

class Game:
    def __init__(self):
        self.Rows = []
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)

    def game_init(self):
        pygame.init()
        pygame.display.set_caption("Breakout")
        pygame.mouse.set_visible(0)
        pygame.event.set_grab(True)

    def game_loop(self):
        Clock = pygame.time.Clock()
        
        Run = True
        while Run:
            delta = Clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.ball_active = True
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

            Gamehelper.update_game_loop(self.ball, self.paddle, delta, self.Rows)
            Gamehelper.update_scorecard()
            pygame.display.update()

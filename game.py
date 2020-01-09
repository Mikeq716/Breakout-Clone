import pygame
import os
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from level import Level
from scorecard import Scorecard

class Game:
    def game_init(self):
        pygame.init()
        pygame.display.set_caption("Breakout")
        pygame.mouse.set_visible(0)
        pygame.event.set_grab(True)

    def game_loop(self, paddle, ball):
        Clock = pygame.time.Clock()
        Rows = []
        level = 1
        ball_active = False

        Level.load_level(50, Rows, level)
        
        Run = True
        while Run:
            delta = Clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ball_active = True
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

            if len(Rows) == 0:
                pygame.time.delay(300)
                level += 1
                Level.load_level(50, Rows, level)
                ball_active = False

            SCREEN.fill((0, 0, 0))
            Scorecard.draw_level(level)

            paddle.update(delta, ball)
            ball.update(delta, paddle)

            ball_active = ball.ball_active(paddle, ball_active, delta)

            Level.update_level(Rows, ball, delta, level)   
            
            pygame.display.update()
           
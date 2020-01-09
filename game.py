import pygame
from config import *
from paddle import Paddle
from ball import Ball
from brick import Brick
from level import Level
from scorecard import Scorecard

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

            Gamehelper.update_game_loop(delta, self.paddle, self.ball, self.Rows)
            Gamehelper.update_scorecard()
            pygame.display.update()


class Gamehelper:
    def update_scorecard():
        Scorecard.draw_score(Scorecard.current_score)
        Scorecard.draw_level(Level.current_level)

    def update_game_loop(delta, paddle, ball, Rows):
        SCREEN.fill((0, 0, 0))
        paddle.update(delta, ball)
        ball.update(delta)
        Level.update_level(ball, delta, Level.current_level, Rows)
        ball.is_ball_active(delta)
        Level.is_level_done(Rows, ball)
           
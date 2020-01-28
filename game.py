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
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)
        self.powerups = []
        self.clock = pygame.time.Clock()
    
    #Initiate pygame in game_init 
    def game_init(self):
        pygame.init()
        pygame.display.set_caption("Breakout")
        pygame.mouse.set_visible(0)
        pygame.event.set_grab(True)

    #game_loop contains the actual game loop
    def game_loop(self):
        Run = True
        while Run:
            delta = self.clock.tick()
            print(delta)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.activate_ball()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

            SCREEN.fill((0, 0, 0))
                    
            if len(self.Rows) == 0:
                self.ball.reset_ball(self.paddle)
                Gamehelper.load_level(self.Rows, self.ball)
                self.powerups.clear()
                self.paddle.reset_paddle_size()

            self.ball.update(self.ball, self.paddle, delta)
            self.paddle.update(delta, self.ball)
        
            for row in self.Rows:
                if len(row) == 0:
                    self.Rows.remove(row)
                for brick in row:
                    brick.update()
                    if self.ball.check_brick_collision(self.ball, brick, delta) == True:
                        Scorecard.add_score(brick.get_value)
                        brick.hit(row, self.powerups)

            for powerup in self.powerups:
                powerup.update(delta, self.paddle, self.powerups)
        
            if Scorecard.lives_left == 1:
                self.paddle.increase_paddle_size()
        
            if Scorecard.lives_left == 0:
                Gamehelper.game_over(self.Rows, self.paddle, self.ball)

            Gamehelper.update_scorecard()
            pygame.display.update()

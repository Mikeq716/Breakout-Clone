import pygame

from .. import config, state_machine
from .. game_functions import GameFunctions
from ..components import scorecard, brick
from ..components.paddle import Paddle
from ..components.ball import Ball
from ..components.level import Level

class Game:
    def __init__(self):
        state_machine.State.__init__(self)
        self.next = "MENU"
        self.paddle = Paddle()
        self.ball_list = []
        Ball.spawn_ball(self.ball_list, self.paddle)
        self.scorecard = scorecard.Scorecard()
        self.current_level = 0
        self.bricks = []
        self.moving_bricks = []
        self.spawned_powerups = []
        self.activated_powerups = []

    def startup(self):
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        if config.NEW_GAME == True:
            GameFunctions.new_game(self)
            config.NEW_GAME = False

    def update(self):
        self.delta = self.clock.tick()
        self.paddle.update(self.delta)
        
        for ball in self.ball_list:
            GameFunctions.check_paddle_collision(ball, self.paddle, self.delta)
            ball.update(self.paddle, self.delta, self.scorecard)
            if ball.missed_ball(self.delta) == True:
                if len(self.ball_list) > 1:
                    self.ball_list.remove(ball)
                else:
                    ball.reset_ball()
                    ball.decrease_speed()
                    self.scorecard.remove_life()
                    GameFunctions.clear_powerups(self)

        GameFunctions.update_level(self)
        GameFunctions.update_powerups(self)
                        
        if config.CURRENT_COUNT == 0:
            GameFunctions.next_level(self)

        if self.scorecard.lives_left == 0:
            GameFunctions.new_game(self)

    def draw(self, surface):
        surface.blit(config.BG_IMGS['background_img'], (0, 0))
        self.paddle.draw(surface)
        self.scorecard.update_scorecard(self.current_level, surface)

        for ball in self.ball_list:
            ball.draw(surface)  
        
        for row in self.bricks:
            for brick in row:
                brick.draw(surface)  

        for powerup in self.spawned_powerups:
            powerup.draw(surface)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                for ball in self.ball_list:
                    ball.reset_ball()
                self.done = True
            if event.key == pygame.K_SPACE:
                for ball in self.ball_list:
                    ball.activate_ball()



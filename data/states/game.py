import pygame

from .. import config, state_machine
from ..components import scorecard, brick
from ..components.paddle import Paddle
from ..components.ball import Ball
from ..components.level import Level
from ..components.powerup import *

class Game:
    def __init__(self):
        state_machine.State.__init__(self)
        self.next = "MENU"
        self.paddle = Paddle()
        self.ball_list = []
        Ball.spawn_ball(self.ball_list, self.paddle)
        self.scorecard = scorecard.Scorecard()
        self.current_level = 0
        self.rows = []
        self.spawned_powerups = []
        self.activated_powerups = []
        self.brick_count = 0

    def startup(self):
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        if config.NEW_GAME == True:
            self.new_game()
            config.NEW_GAME = False

    def update(self):
        self.delta = self.clock.tick()
        self.paddle.update(self.delta)

        for ball in self.ball_list:
            ball.update(ball, self.delta, self.scorecard)
            if ball.missed_ball(self.delta) == True:
                if len(self.ball_list) > 1:
                    self.ball_list.remove(ball)
                else:
                    self.clear_powerups()
                    self.scorecard.remove_life()
                    ball.reset_ball()
                    ball.decrease_speed()
        
        if self.scorecard.lives_left == 0:
            self.new_game()
        
        for row in self.rows:
            if len(row) == 0:
                self.rows.remove(row)
            for brick in row:
                for ball in self.ball_list:
                    if ball.check_brick_collision(ball, brick, self.delta) == True: 
                        self.scorecard.add_score(brick.get_value)
                        if brick.locked == False:
                            Powerup.spawn_powerup(self.spawned_powerups, brick.get_pos)
                            row.remove(brick)
                            config.CURRENT_COUNT -= 1
        
        for powerup in self.spawned_powerups:
            powerup.update_spawned_powerups(self.delta, self.spawned_powerups, self.activated_powerups, self.paddle)
        
        for powerup in self.activated_powerups:
            if powerup.activated == False:
                powerup.activate(self.paddle, self.ball_list, self.scorecard)
            if powerup.activated == True:
                powerup.update(self.activated_powerups, self.paddle, self.ball_list, self.scorecard, self.delta)
        
        if config.CURRENT_COUNT == 0:
            self.clear_powerups()
            Level.new_level(self.current_level, self.rows)
            self.paddle.reset_paddle_size()
            self.current_level += 1
            for ball in self.ball_list:
                ball.reset_ball()
                ball.increase_speed()

    def draw(self, surface):
        surface.blit(config.BG_IMGS['background_img'], (0, 0))
        self.paddle.draw(surface)
        
        for ball in self.ball_list:
            ball.draw(surface)  
        
        self.scorecard.update_scorecard(self.current_level, surface)
        
        for row in self.rows:
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

    def new_game(self):
        self.clear_powerups()
        self.spawned_powerups.clear()
        self.activated_powerups.clear()
        config.CURRENT_COUNT = 0
        self.new = False
        self.rows.clear()
        self.current_level = 0
        self.scorecard.lives_left = 3
        self.scorecard.current_score = 0
        self.paddle.reset_paddle_size()
        for ball in self.ball_list:
            ball.reset_speed()

    def clear_powerups(self):
        for powerup in self.activated_powerups:
            powerup.deactivate(self.paddle, self.ball_list)
        self.activated_powerups.clear()
        self.spawned_powerups.clear()


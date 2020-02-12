import pygame

from .. import config, state_machine
from ..components import paddle, ball, scorecard, level, brick
from ..components.powerup import *

class Game:
    def __init__(self):
        state_machine.State.__init__(self)
        self.next = "MENU"
        self.paddle = paddle.Paddle()
        self.ball = ball.Ball(self.paddle)
        self.scorecard = scorecard.Scorecard()
        self.level = level.Level()
        self.current_level = 0
        self.rows = []
        self.spawned_powerups = []
        self.activated_powerups = []

    def startup(self):
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        if config.NEW_GAME == True:
            self.new_game()
            config.NEW_GAME = False

    def update(self):
        self.delta = self.clock.tick()
        self.paddle.update(self.delta)
        self.ball.update(self.ball, self.paddle, self.delta, self.scorecard)

        if self.scorecard.lives_left == 0:
            self.new_game()
        
        for row in self.rows:
            if len(row) == 0:
                self.rows.remove(row)
            for brick in row:
                if self.ball.check_brick_collision(self.ball, brick, self.delta) == True: 
                    self.scorecard.add_score(brick.get_value)
                    Powerup.spawn_powerup(self.spawned_powerups, brick.get_pos)
                    brick.hit(row)

        for powerup in self.spawned_powerups:
            powerup.update_spawned_powerups(self.delta, self.spawned_powerups, self.activated_powerups, self.paddle)

        for powerup in self.activated_powerups:
            if powerup.activated == False:
                powerup.activate(self.paddle, self.ball, self.scorecard)
            if powerup.activated == True:
                powerup.update(self.activated_powerups, self.paddle, self.ball, self.scorecard, self.delta)
        
        if len(self.rows) == 0:
            self.ball.reset_ball(self.paddle)
            self.level.new_level(self.current_level, self.rows)
            self.ball.increase_speed()
            self.paddle.reset_paddle_size()
            self.current_level += 1

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.paddle.draw(surface)
        self.ball.draw(surface)
        self.level.draw_level(self.rows, surface)
        self.scorecard.update_scorecard(self.current_level, surface)

        for powerup in self.spawned_powerups:
            powerup.draw(surface)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.ball.reset_ball(self.paddle)
                self.done = True
            if event.key == pygame.K_SPACE:
                self.ball.activate_ball()

    def new_game(self):
        self.new = False
        self.rows.clear()
        self.current_level = 0
        self.scorecard.lives_left = 3
        self.scorecard.current_score = 0
        self.paddle.reset_paddle_size()
        self.ball.reset_speed()
        
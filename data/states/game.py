import pygame

from .. import config, state_machine
from ..components import paddle, ball, scorecard, level, brick

class Game:
    def __init__(self):
        state_machine.State.__init__(self)
        self.next = "MENU"
        self.clock = pygame.time.Clock()

    def startup(self):
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        self.paddle = paddle.Paddle()
        self.ball = ball.Ball(self.paddle)
        self.scorecard = scorecard.Scorecard()
        self.level = level.Level()
        self.current_level = 0
        self.rows = []

    def cleanup(self):
        pass

    def update(self):
        self.delta = self.clock.tick()
        self.paddle.update(self.delta)

        if len(self.rows) == 0:
            self.ball.reset_ball(self.paddle)
            self.level.new_level(self.current_level, self.rows)
            self.ball.increase_speed()
            self.paddle.reset_paddle_size()
            self.current_level += 1

        for row in self.rows:
            if len(row) == 0:
                self.rows.remove(row)
            for brick in row:
                if self.ball.check_brick_collision(self.ball, brick, self.delta) == True:
                    self.scorecard.add_score(brick.get_value)
                    brick.hit(row)

        self.ball.update(self.ball, self.paddle, self.delta)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.paddle.draw(surface)
        self.ball.draw(surface)
        self.scorecard.update_scorecard(self.current_level, surface)
        for row in self.rows:
            for brick in row:
                brick.update(surface)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.done = True
            if event.key == pygame.K_SPACE:
                self.ball.activate_ball()
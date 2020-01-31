import pygame
import sys
from game import Game
from paddle import Paddle
from ball import Ball

class States:
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None


class Menu(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'main_game'

    def cleanup(self):
        pass

    def startup(self):
        pass

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True

    def update(self, dt):
        pass
    

class Main_Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'
        self.game = Game()
        self.paddle = Paddle()
        self.ball = Ball(self.paddle)

    def cleanup(self):
        pass

    def startup(self):
        pass

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
            elif event.key == pygame.K_SPACE:
                self.ball.activate_ball()

    def update(self, dt):     
        self.game.game_loop(dt, self.ball, self.paddle)

class Control:
    def __init__(self, **settings):
        self.__dict__.update(settings)
        self.done = False
        self.clock = pygame.time.Clock()
    
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)

    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick()
            self.event_loop()
            self.update(delta_time)
            pygame.display.update()


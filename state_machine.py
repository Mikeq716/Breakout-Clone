import pygame
import sys
from game import Game
from paddle import Paddle
from ball import Ball
from config import *

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
        self.exit = SCREEN.blit(exit_img, (200, 350))
        self.start = SCREEN.blit(start_game_img, (200, 50))

    def startup(self):
        pass

    def cleanup(self):
        pass

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if self.start.collidepoint(pos):
                self.done = True
            if self.exit.collidepoint(pos):
                self.quit = True
        if event.type == pygame.QUIT:
            self.quit = True

    def update(self, dt):
        pygame.mouse.set_visible(1)
        pygame.event.set_grab(False)
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(start_game_img, (200, 50))
        SCREEN.blit(exit_img, (200, 350))
    

class Main_Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'

    def startup(self):
        self.game = Game()

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.ball.activate_ball()
            elif event.key == pygame.K_ESCAPE:
                self.done = True

    def update(self, dt):
        pygame.mouse.set_visible(0)
        pygame.event.set_grab(True)     
        self.game.run_game(dt)


class Control:
    def __init__(self):
        self.done = False
        self.clock = pygame.time.Clock()
    
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
            self.state.get_event(event)

    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick()
            self.event_loop()
            self.update(delta_time)
            pygame.display.update()


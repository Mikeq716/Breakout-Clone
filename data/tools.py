import os
import pygame

from . import state_machine


class Control:
    def __init__(self, caption):
        self.screen = pygame.display.get_surface()
        self.caption = caption
        self.done = False
        self.state_machine = state_machine.StateMachine()

    def update(self):
        self.done = self.state_machine.done
        self.state_machine.update()

    def draw(self):
        if not self.state_machine.state.done:
            self.state_machine.draw(self.screen)
            pygame.display.update()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.state_machine.get_event(event)

    def main(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()

        


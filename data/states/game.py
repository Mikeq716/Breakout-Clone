import pygame

from .. import config, state_machine

class Game:
    def __init__(self):
        state_machine.State.__init__(self)
        self.next = "MENU"

    def update(self):
        pass

    def startup(self):
        pass

    def cleanup(self):
        pass

    def draw(self, surface):
        surface.fill((0, 0, 0))

    def get_event(self, event):
        pass
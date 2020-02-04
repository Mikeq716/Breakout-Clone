import pygame

from .. import config, state_machine

class Game:
    def __init__(self):
        state_machine.State.__init__(self)
        self.next = "MENU"

    def update(self):
        pass

    def draw(self, surface):
        pass

    def get_event(self, event):
        pass
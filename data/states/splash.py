import pygame

from .. import config, state_machine


class Splash(state_machine.State):
    def __init__(self):
        state_machine.State.__init__(self)
        self.next = "MENU"
        self.clock = pygame.time.Clock()
        self.time = 0

    def update(self):
        self.time += self.clock.tick()
        if self.time >= 3000:
            self.done = True

    def draw(self, surface):
        surface.blit(config.BG_IMGS['splash_img'], (0, 0))

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
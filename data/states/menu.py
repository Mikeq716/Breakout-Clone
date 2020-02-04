import pygame

from .. import config, state_machine


class Menu(state_machine.State):
    def __init__(self):
        state_machine.State.__init__(self)
        self.next = "GAME"

    def update(self):
        pass

    def draw(self, surface):
        self.start_button = surface.blit(config.MENU_IMGS['start_game_img'], (200, 50))
        self.exit_button = surface.blit(config.MENU_IMGS['exit_img'], (200, 350))

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.exit_button.collidepoint(pos):
                self.quit = True
                
                
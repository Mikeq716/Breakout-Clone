import pygame

from .. import config, state_machine


class Menu(state_machine.State):
    def __init__(self):
        state_machine.State.__init__(self)
        self.next = "GAME"

    def startup(self):
        pygame.event.set_grab(False)
        pygame.mouse.set_visible(True)

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.start_button = surface.blit(config.MENU_IMGS['start_game_img'], (200, 50))
        self.exit_button = surface.blit(config.MENU_IMGS['exit_img'], (200, 350))

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.exit_button.collidepoint(pos):
                self.quit = True
            if self.start_button.collidepoint(pos):
                self.done = True
                
                
import pygame

from .. import config, state_machine


class Menu(state_machine.State):
    def __init__(self):
        state_machine.State.__init__(self)
        self.next = "GAME"
        self.surface = pygame.display.get_surface()

    def startup(self):
        pygame.event.set_grab(False)
        pygame.mouse.set_visible(True)
        self.new_game_button = self.surface.blit(config.MENU_IMGS['new_game_img'], (200, 50))
        self.resume_game_button = self.surface.blit(config.MENU_IMGS['resume_game_img'], (200, 225))
        self.exit_button = self.surface.blit(config.MENU_IMGS['exit_img'], (200, 400))

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(config.BG_IMGS['background_img'], (0, 0))
        if self.new_game_button.collidepoint(pygame.mouse.get_pos()):
            surface.blit(config.MENU_IMGS['new_game_selected_img'], (200, 50))
        else:
            surface.blit(config.MENU_IMGS['new_game_img'], (200, 50))
        if self.resume_game_button.collidepoint(pygame.mouse.get_pos()):
            surface.blit(config.MENU_IMGS['resume_game_selected_img'], (200, 225))
        else:
            surface.blit(config.MENU_IMGS['resume_game_img'], (200, 225))
        if self.exit_button.collidepoint(pygame.mouse.get_pos()):
            self.surface.blit(config.MENU_IMGS['exit_selected_img'], (200, 400))
        else:
            self.surface.blit(config.MENU_IMGS['exit_img'], (200, 400))

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.new_game_button.collidepoint(pos):
                config.NEW_GAME = True
                self.done = True
            if self.resume_game_button.collidepoint(pos):
                self.done = True
            if self.exit_button.collidepoint(pos):
                self.quit = True
                
                
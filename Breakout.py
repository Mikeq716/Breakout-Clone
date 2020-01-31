import pygame
from config import *
from game import Game
from state_machine import *

def main():
    settings = {
        'size': (800, 600)
    }

    state_dict = {
        'menu': Menu()
    }

    app = Control(**settings)
    app.setup_states(state_dict, 'menu')
    app.main_game_loop()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

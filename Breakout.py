import pygame
from config import *
from state_machine import *

def main():
    state_dict = {
        'menu': Menu(),
        'main_game': Main_Game()
    }

    pygame.init()
    pygame.display.set_caption("Breakout")

    app = Control()
    app.setup_states(state_dict, 'menu')
    app.main_game_loop()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

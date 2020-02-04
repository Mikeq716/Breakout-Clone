from . import tools
from .states import menu, game


def main():
    app = tools.Control("Breakout")
    
    state_dict = {"MENU" : menu.Menu(),
                  "GAME" : game.Game()
    }

    app.state_machine.setup_states(state_dict, "MENU")
    app.main()
from . import tools, config
from .states import menu, game, splash


def main():
    app = tools.Control(config.CAPTION)
    
    state_dict = {"MENU" : menu.Menu(),
                  "GAME" : game.Game(),
                  "SPLASH" : splash.Splash()
    }

    app.state_machine.setup_states(state_dict, "SPLASH")
    app.main()
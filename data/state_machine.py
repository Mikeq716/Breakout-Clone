import pygame
import sys
    

class StateMachine:
    def __init__(self):
        self.done = False
        self.state_dict = {}
        self.state_name = None
        self.state = None
    
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def draw(self, surface):
        self.state.draw(surface)

    def flip_state(self):
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update()

    def get_event(self, event):
        self.state.get_event(event)


class State:
    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}

    def get_event(self, event):
        pass

    def startup(self, persistant):
        self.persist = persistant

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self):
        pass

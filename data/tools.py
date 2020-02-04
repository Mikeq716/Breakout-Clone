import os
import pygame

from . import state_machine


class Control:
    def __init__(self, caption):
        self.screen = pygame.display.get_surface()
        self.caption = caption
        self.done = False
        self.clock = pygame.time.Clock()
        self.state_machine = state_machine.StateMachine()

    def update(self):
        self.state_machine.update()

    def draw(self):
        if not self.state_machine.state.done:
            self.state_machine.draw(self.screen)
            pygame.display.update()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.state_machine.get_event(event)

    def main(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()


def load_all_images():
    images = {"paddle_smallest_img" : pygame.image.load(os.path.join('images/paddles/', 'paddle_smallest.png')).convert_alpha()
              "paddle_smaller_img" : pygame.image.load(os.path.join('images/paddles/', 'paddle_smaller.png')).convert_alpha()
              "paddle_img" : pygame.image.load(os.path.join('images/paddles/', 'paddle.png')).convert_alpha()
              "paddle_large_img" : pygame.image.load(os.path.join('images/paddles/', 'paddle_large.png')).convert_alpha()
              "ball_img" : pygame.image.load(os.path.join('images/', 'ball.png')).convert_alpha()
              "brick_blue_img" : pygame.image.load(os.path.join('images/bricks/', 'brick_blue.png')).convert_alpha()
              "brick_green_img" : pygame.image.load(os.path.join('images/bricks/', 'brick_green.png')).convert_alpha()
              "brick_orange_img" : pygame.image.load(os.path.join('images/bricks/', 'brick_orange.png')).convert_alpha()
              "brick_pink_img" : pygame.image.load(os.path.join('images/bricks/', 'brick_pink.png')).convert_alpha()
              "brick_purple_img" : pygame.image.load(os.path.join('images/bricks/', 'brick_purple.png')).convert_alpha()
              "brick_red_img" : pygame.image.load(os.path.join('images/bricks/', 'brick_red.png')).convert_alpha()
              "brick_yellow_img" : pygame.image.load(os.path.join('images/bricks/', 'brick_yellow.png')).convert_alpha()
              "powerup_health_img" : pygame.image.load(os.path.join('images/powerups/', 'health.png')).convert_alpha()
              "powerup_increase_paddle_img" : pygame.image.load(os.path.join('images/powerups/', 'increase_paddle.png')).convert_alpha()
              "powerup_decrease_paddle_img" : pygame.image.load(os.path.join('images/powerups/', 'decrease_paddle.png')).convert_alpha()
              "start_game_img" : pygame.image.load(os.path.join('images/menu/', 'start_game.png')).convert_alpha()
              "exit_img" : pygame.image.load(os.path.join('images/menu/', 'exit.png')).convert_alpha()
    }
    return images
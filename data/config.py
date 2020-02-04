import os
import pygame

from . import tools

#config.py
#Definitions of all constants and paths to images

pygame.init()

SCREEN_SIZE = (800, 600)
CAPTION = "Breakout"
SCREEN_RECT = pygame.Rect((0, 0), SCREEN_SIZE)

pygame.display.set_caption(CAPTION)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

#Initiate pygames font module and create the font used for the scorecard
pygame.font.init()
font = pygame.font.SysFont('comic.ttf', 26)

#Load various game images
paddle_smallest_img = pygame.image.load(os.path.join('images/paddles/', 'paddle_smallest.png')).convert_alpha()
paddle_smaller_img = pygame.image.load(os.path.join('images/paddles/', 'paddle_smaller.png')).convert_alpha()
paddle_img = pygame.image.load(os.path.join('images/paddles/', 'paddle.png')).convert_alpha()
paddle_large_img = pygame.image.load(os.path.join('images/paddles/', 'paddle_large.png')).convert_alpha()
ball_img = pygame.image.load(os.path.join('images/', 'ball.png')).convert_alpha()
brick_blue_img = pygame.image.load(os.path.join('images/bricks/', 'brick_blue.png')).convert_alpha()
brick_green_img = pygame.image.load(os.path.join('images/bricks/', 'brick_green.png')).convert_alpha()
brick_orange_img = pygame.image.load(os.path.join('images/bricks/', 'brick_orange.png')).convert_alpha()
brick_pink_img = pygame.image.load(os.path.join('images/bricks/', 'brick_pink.png')).convert_alpha()
brick_purple_img = pygame.image.load(os.path.join('images/bricks/', 'brick_purple.png')).convert_alpha()
brick_red_img = pygame.image.load(os.path.join('images/bricks/', 'brick_red.png')).convert_alpha()
brick_yellow_img = pygame.image.load(os.path.join('images/bricks/', 'brick_yellow.png')).convert_alpha()
powerup_health_img = pygame.image.load(os.path.join('images/powerups/', 'health.png')).convert_alpha()
powerup_increase_paddle_img = pygame.image.load(os.path.join('images/powerups/', 'increase_paddle.png')).convert_alpha()
powerup_decrease_paddle_img = pygame.image.load(os.path.join('images/powerups/', 'decrease_paddle.png')).convert_alpha()
start_game_img = pygame.image.load(os.path.join('images/menu/', 'start_game.png')).convert_alpha()
exit_img = pygame.image.load(os.path.join('images/menu/', 'exit.png')).convert_alpha()

IMAGES = {1: brick_blue_img, 2: brick_green_img, 3: brick_orange_img, 4: brick_pink_img, 5: brick_purple_img, 6: brick_red_img, 7: brick_yellow_img}

PADDLE_Y = 550

BALL_WIDTH = ball_img.get_width()
BALL_HEIGHT = ball_img.get_height()

BRICK_WIDTH = brick_blue_img.get_width()
BRICK_HEIGHT = brick_blue_img.get_height()
    
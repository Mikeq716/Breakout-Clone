import os
import pygame

#config.py
#Definitions of all constants and paths to images

#Initiate pygames font module and create the font used for the scorecard
pygame.font.init()
font = pygame.font.SysFont('comic.ttf', 26)

#Load various game images
paddle_smallest_img = pygame.image.load(os.path.join('images/paddles/', 'paddle_smallest.png'))
paddle_smaller_img = pygame.image.load(os.path.join('images/paddles/', 'paddle_smaller.png'))
paddle_img = pygame.image.load(os.path.join('images/paddles/', 'paddle.png'))
paddle_large_img = pygame.image.load(os.path.join('images/paddles/', 'paddle_large.png'))
ball_img = pygame.image.load(os.path.join('images/', 'ball.png'))
brick_blue_img = pygame.image.load(os.path.join('images/bricks/', 'brick_blue.png'))
brick_green_img = pygame.image.load(os.path.join('images/bricks/', 'brick_green.png'))
brick_orange_img = pygame.image.load(os.path.join('images/bricks/', 'brick_orange.png'))
brick_pink_img = pygame.image.load(os.path.join('images/bricks/', 'brick_pink.png'))
brick_purple_img = pygame.image.load(os.path.join('images/bricks/', 'brick_purple.png'))
brick_red_img = pygame.image.load(os.path.join('images/bricks/', 'brick_red.png'))
brick_yellow_img = pygame.image.load(os.path.join('images/bricks/', 'brick_yellow.png'))
powerup_health_img = pygame.image.load(os.path.join('images/powerups/', 'health.png'))
powerup_increase_paddle_img = pygame.image.load(os.path.join('images/powerups/', 'increase_paddle.png'))
powerup_decrease_paddle_img = pygame.image.load(os.path.join('images/powerups/', 'decrease_paddle.png'))

IMAGES = {1: brick_blue_img, 2: brick_green_img, 3: brick_orange_img, 4: brick_pink_img, 5: brick_purple_img, 6: brick_red_img, 7: brick_yellow_img}

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

PADDLE_Y = 550

BALL_WIDTH = ball_img.get_width()
BALL_HEIGHT = ball_img.get_height()

BRICK_WIDTH = brick_blue_img.get_width()
BRICK_HEIGHT = brick_blue_img.get_height()
    
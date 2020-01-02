import os
import pygame

#config.py
#Definitions of all constants and paths to images

#Load various game images
paddle_img = pygame.image.load(os.path.join('images/', 'paddle.png'))
ball_img = pygame.image.load(os.path.join('images/', 'ball.png'))
brick_blue_img = pygame.image.load(os.path.join('images/', 'brick_blue.png'))
brick_green_img = pygame.image.load(os.path.join('images/', 'brick_blue.png'))
brick_orange_img = pygame.image.load(os.path.join('images/', 'brick_orange.png'))
brick_pink_img = pygame.image.load(os.path.join('images/', 'brick_pink.png'))
brick_purple_img = pygame.image.load(os.path.join('images/', 'brick_purple.png'))
brick_red_img = pygame.image.load(os.path.join('images/', 'brick_red.png'))
brick_yellow_img = pygame.image.load(os.path.join('images/', 'brick_yellow.png'))

SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

PADDLE_Y = 550
PADDLE_SPEED = 2
PADDLE_WIDTH = paddle_img.get_width()

BALL_SPEED = 3
BALL_WIDTH = ball_img.get_width()
BALL_HEIGHT = ball_img.get_height()
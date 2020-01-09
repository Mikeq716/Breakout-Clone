import os
import pygame

#config.py
#Definitions of all constants and paths to images
pygame.font.init()

#Load various game images
paddle_img = pygame.image.load(os.path.join('images/', 'paddle.png'))
ball_img = pygame.image.load(os.path.join('images/', 'ball.png'))
brick_blue_img = pygame.image.load(os.path.join('images/', 'brick_blue.png'))
brick_green_img = pygame.image.load(os.path.join('images/', 'brick_green.png'))
brick_orange_img = pygame.image.load(os.path.join('images/', 'brick_orange.png'))
brick_pink_img = pygame.image.load(os.path.join('images/', 'brick_pink.png'))
brick_purple_img = pygame.image.load(os.path.join('images/', 'brick_purple.png'))
brick_red_img = pygame.image.load(os.path.join('images/', 'brick_red.png'))
brick_yellow_img = pygame.image.load(os.path.join('images/', 'brick_yellow.png'))

font = pygame.font.SysFont('comic.ttf', 26)

IMAGES = {1: brick_blue_img, 2: brick_green_img, 3: brick_orange_img, 4: brick_pink_img, 5: brick_purple_img, 6: brick_red_img, 7: brick_yellow_img}
BRICK_VALUES = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

PADDLE_Y = 550
PADDLE_WIDTH = paddle_img.get_width()

BALL_SPEED = 0.75
BALL_WIDTH = ball_img.get_width()
BALL_HEIGHT = ball_img.get_height()

BRICK_WIDTH = brick_blue_img.get_width()
BRICK_HEIGHT = brick_blue_img.get_height()

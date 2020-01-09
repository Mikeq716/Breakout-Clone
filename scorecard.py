import pygame
from config import *

class Scorecard:
    def draw_level(level):
        white = (255, 255, 255) 
        font = pygame.font.Font('freesansbold.ttf', 26)
        score = font.render('Level: ' + str(level), True, white)
        scoreRect = score.get_rect()
        scoreRect.center = (100, 20)
        SCREEN.blit(score, scoreRect)

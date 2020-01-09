import pygame
from config import *

class Scorecard:
    current_score = 0

    def draw_score(score):
        white = (255, 255, 255)
        score = font.render('Score: ' + str(score), True, white)
        scoreRect = score.get_rect()
        scoreRect.center = (100, 20)
        SCREEN.blit(score, scoreRect)

    def draw_level(level):
        white = (255, 255, 255)
        level = font.render('Level: ' + str(level), True, white)
        levelRect = level.get_rect()
        levelRect.center = (600, 20)
        SCREEN.blit(level, levelRect)
        

    

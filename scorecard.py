import pygame
from config import *

class Scorecard:
    current_score = 0
    lives_left = 3

    def draw_score(score):
        white = (255, 255, 255)
        score = font.render('Score: ' + str(score), True, white)
        scoreRect = score.get_rect()
        scoreRect.center = (100, 20)
        SCREEN.blit(score, scoreRect)

    def draw_lives(lives_left):
        white = (255, 255, 255)
        lives = font.render('Lives Left: ' + str(lives_left), True, white)
        livesRect = lives.get_rect()
        livesRect.center = (300, 20)
        SCREEN.blit(lives, livesRect)

    def draw_level(level):
        white = (255, 255, 255)
        level = font.render('Level: ' + str(level), True, white)
        levelRect = level.get_rect()
        levelRect.center = (600, 20)
        SCREEN.blit(level, levelRect)
        
    def add_score(amount):
        Scorecard.current_score += amount

    def add_life():
        Scorecard.lives_left += 1
    

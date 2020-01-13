import pygame
from config import *

class Scorecard:
    current_score = 0
    lives_left = 3

    #Function Draw Score
    #Function Draw Score draws to current score to the screen for the current frame
    def draw_score(score):
        white = (255, 255, 255)
        score = font.render('Score: ' + str(score), True, white)
        scoreRect = score.get_rect()
        scoreRect.center = (100, 20)
        SCREEN.blit(score, scoreRect)

    #Function Draw Lives
    #Function Draw Lives draws the current lives left to the screen for the current frame
    def draw_lives(lives_left):
        white = (255, 255, 255)
        lives = font.render('Lives Left: ' + str(lives_left), True, white)
        livesRect = lives.get_rect()
        livesRect.center = (300, 20)
        SCREEN.blit(lives, livesRect)

    #Function Draw Level
    #Function Draw Level draws the current level to the screen for the current frame
    def draw_level(level):
        white = (255, 255, 255)
        level = font.render('Level: ' + str(level), True, white)
        levelRect = level.get_rect()
        levelRect.center = (600, 20)
        SCREEN.blit(level, levelRect)

    #Function Add Score
    #Function Add Score adds the hit bricks value to the current score    
    def add_score(amount):
        Scorecard.current_score += amount

    #Function Add Life
    #Function Add Life adds 1 life to current lives left
    def add_life():
        Scorecard.lives_left += 1
    

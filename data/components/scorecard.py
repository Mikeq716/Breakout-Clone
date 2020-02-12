import pygame

from .. import config

class Scorecard:
    current_score = 0
    lives_left = 3

    #Function Draw Score
    #Function Draw Score draws to current score to the screen for the current frame
    def draw_score(self, surface):
        text_color = (191, 191, 191)
        score = config.font.render('Score: ' + str(self.current_score), True, text_color)
        scoreRect = score.get_rect()
        scoreRect.center = (100, 20)
        surface.blit(score, scoreRect)

    #Function Draw Lives
    #Function Draw Lives draws the current lives left to the screen for the current frame
    def draw_lives(self, surface):
        text_color = (191, 191, 191)
        lives = config.font.render('Lives Left: ' + str(self.lives_left), True, text_color)
        livesRect = lives.get_rect()
        livesRect.center = (300, 20)
        surface.blit(lives, livesRect)

    #Function Draw Level
    #Function Draw Level draws the current level to the screen for the current frame
    def draw_level(self, level, surface):
        text_color = (191, 191, 191)
        level = config.font.render('Level: ' + str(level), True, text_color)
        levelRect = level.get_rect()
        levelRect.center = (600, 20)
        surface.blit(level, levelRect)

    #Function Add Score
    #Function Add Score adds the hit bricks value to the current score    
    def add_score(self, amount):
        self.current_score += amount

    #Function Add Life
    #Function Add Life adds 1 life to current lives left
    def add_life(self):
        self.lives_left += 1

    def remove_life(self):
        self.lives_left -= 1

    def update_scorecard(self, level, surface):
        self.draw_lives(surface)
        self.draw_score(surface)
        self.draw_level(level, surface)
    

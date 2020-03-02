import pygame

from .. import config

class Scorecard:
    current_score = 0
    lives_left = 3

    #Function Draw Score draws to current score to the screen for the current frame
    def draw_score(self, surface):
        score = config.font.render('Score: ' + str(self.current_score), True, config.TEXT_COLOR)
        scoreRect = score.get_rect()
        scoreRect.center = (100, 20)
        surface.blit(score, scoreRect)

    #Function Draw Lives draws the current lives left to the screen for the current frame
    def draw_lives(self, surface):
        lives = config.font.render('Lives Left: ' + str(self.lives_left), True, config.TEXT_COLOR)
        livesRect = lives.get_rect()
        livesRect.center = (300, 20)
        surface.blit(lives, livesRect)

    #Function Draw Level draws the current level to the screen for the current frame
    def draw_level(self, level, surface):
        level = config.font.render('Level: ' + str(level), True, config.TEXT_COLOR)
        levelRect = level.get_rect()
        levelRect.center = (600, 20)
        surface.blit(level, levelRect)

    #Function Add Score adds the hit bricks value to the current score    
    def add_score(self, amount):
        self.current_score += amount

    #Function Add Life adds 1 life to current lives left
    def add_life(self):
        self.lives_left += 1

    #Function Remove Life removes 1 life from the current lives left
    def remove_life(self):
        self.lives_left -= 1

    #Function Update Scorecard draws lives, current score, and current level each frame
    def update_scorecard(self, level, surface):
        self.draw_lives(surface)
        self.draw_score(surface)
        self.draw_level(level, surface)
    

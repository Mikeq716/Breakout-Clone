import pygame
from config import *

#Paddle class definition

class Paddle:
    def __init__(self):
        self.__x = SCREEN_WIDTH / 2
        self.__y = PADDLE_Y
        self.__current_size = 3
        self.__current_img = PADDLE_IMG[self.__current_size]
        self.__width = self.__current_img.get_width()

    #Function Get Pos 
    #Function Get Pos returns the paddles current x position
    @property
    def get_pos(self):
        return self.__x

    #Function Get Width
    #Function Get Width returns the paddles current width
    @property
    def get_width(self):
        return self.__width

    #Function Update
    #Function Update calculates paddles movement, sets the paddles image depending on size, updates its __width variable, and draws it to the screen
    def update(self, delta, ball):
        self.__move()
        self.__current_img = PADDLE_IMG[self.__current_size]
        self.__width = self.__current_img.get_width()
        SCREEN.blit(self.__current_img, [self.__x, self.__y])

    #Function Increase Paddle Size
    #Function Increase Paddle Size increases the paddles size if its not at its maximum
    def increase_paddle_size(self):
        if self.__current_size == 4:
            pass
        else:
            self.__current_size += 1

    #Function Decrease Paddle Size
    #Function Decrease Paddle Size decreases the paddles size if its not at its minimum
    def decrease_paddle_size(self):
        if self.__current_size == 1:
            pass
        else:
            self.__current_size -= 1

    #Function Reset Paddle Size
    #Function Reset Paddle Size resets the paddles size to its normal size
    def reset_paddle_size(self):
        if self.__current_size != 3:
            self.__current_size = 3

    #Function Move
    #Function Move calculates the paddles new position based on mouse movement for the current frame
    def __move(self):
        paddle_move = pygame.mouse.get_rel()
        self.__x += paddle_move[0] * 0.5
        if self.__x < 0:
            self.__x = 0
        elif self.__x >= SCREEN_WIDTH - self.__width:
            self.__x = SCREEN_WIDTH - self.__width

    
PADDLE_IMG = {1: paddle_smallest_img, 2: paddle_smaller_img, 3: paddle_img, 4: paddle_large_img}
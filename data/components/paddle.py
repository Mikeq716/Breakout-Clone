import pygame
from .. import config


class Paddle:
    def __init__(self):
        self.__x = config.SCREEN_WIDTH / 2
        self.__y = config.PADDLE_Y
        self.__current_size = 3
        self.__current_img = CURRENT_IMG[self.__current_size]
        self.__width = self.__current_img.get_width()

    #Function Get Pos returns the paddles current x position
    @property
    def get_pos(self):
        return self.__x

    #Function Get Width returns the paddles current width
    @property
    def get_width(self):
        return self.__width

    #Function Update calculates paddles movement, sets the paddles image depending on size, updates its __width variable, and draws it to the screen
    def update(self, delta):
        #Set the paddles image based on its current size
        self.__current_img = CURRENT_IMG[self.__current_size]
        #Calculate the pixel width of the paddle based on its current size
        self.__width = self.__current_img.get_width()
        #Calculate the paddles position for the current frame
        self.__move()

    #Function Move calculates the paddles new position based on mouse movement for the current frame
    def __move(self):
        #Set paddle_move equal to how far the mouse moved this frame
        paddle_move = pygame.mouse.get_rel()
        #Add paddle_move multiplied by 0.5(to control speed) to the current x position
        self.__x += paddle_move[0] * 0.5
        #If the paddle would move past either side of the screen, don't let it
        if self.__x < 0:
            self.__x = 0
        elif self.__x >= config.SCREEN_WIDTH - self.__width:
            self.__x = config.SCREEN_WIDTH - self.__width

    #Function Draw blits the paddle onto the screen
    def draw(self, surface):
        surface.blit(self.__current_img, [self.__x, self.__y])

    #Function Increase Paddle Size increases the paddles size if its not at its maximum
    def increase_paddle_size(self):
        if self.__current_size == 4:
            pass
        else:
            self.__current_size += 1

    #Function Decrease Paddle Size decreases the paddles size if its not at its minimum
    def decrease_paddle_size(self):
        if self.__current_size == 1:
            pass
        else:
            self.__current_size -= 1

    #Function Reset Paddle Size resets the paddles size to its normal size
    def reset_paddle_size(self):
        if self.__current_size != 3:
            self.__current_size = 3


CURRENT_IMG = { 1 : config.PADDLE_IMGS['paddle_smallest_img'],
                2 : config.PADDLE_IMGS['paddle_smaller_img'],
                3 : config.PADDLE_IMGS['paddle_img'],
                4 : config.PADDLE_IMGS['paddle_large_img']
}
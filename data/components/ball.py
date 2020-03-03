import pygame
import random

from .. import config

#Ball class definition
class Ball:
    def __init__(self, paddle):
        self.img = config.BALL_IMGS['ball_img']
        self.size = self.img.get_width()
        self.position = pygame.math.Vector2(paddle.get_pos + paddle.get_width / 2 + self.size / 2)
        self.direction = pygame.math.Vector2(random.uniform(-0.75, 0.75), -1).normalize()
        self.ball_active = False
        self.ball_speed = 0.5
        self.nuclear = False
        self.rapidball = False
        self.sticky_paddle = False
        self.__paddle = paddle

    #Update function calculates new position and draws ball, checks for paddle collision and checks if ball is active
    def update(self, paddle, delta, scorecard):
        #Set self.size equal to the size of the current ball image
        self.size = self.img.get_width()
        #If the ball is currently active, then calculate its movement for the current frame
        if self.ball_active == True:
            self.__move(delta)
        #If the ball is not currently active, then call deactive ball to move it to the center of the paddle
        if self.ball_active == False:
            self.deactivate_ball(delta)

    #Function Move reverses the balls direction if it hits a wall and calculates the balls movement for the current frame
    def __move(self, delta):        
        #If the balls calculated x position is greater then the width of the screen, reverse the x direction
        if self.position.x + self.size + self.direction.x * self.ball_speed * delta >= 800:
            self.direction.x *= -1
        #If the balls calculated x position is less than 0, reverse the x direction
        if self.position.x + self.direction.x * self.ball_speed * delta <= 0:
            self.direction.x *= -1
        #If the balls calculated y position is less than the bottom of the scoreboard, reverse the y direction
        if self.position.y + self.direction.y * self.ball_speed * delta <= 35:
            self.direction.y *= -1
        #Set the balls posititon for the current frame            
        self.position += self.direction * self.ball_speed * delta
        
    #Function Draw blits the ball to the screen
    def draw(self, surface):
        surface.blit(self.img, self.position)

    #Function Spawn_Ball will spawn a ball and add it to the list of balls
    def spawn_ball(ball_list, paddle):
        ball = Ball(paddle)
        #If there are other balls active, spawn the ball as active
        if len(ball_list) > 0:
            ball.ball_active = True
        #Append the new ball to the current list of active balls
        ball_list.append(ball)

    #Activate Ball Function sets the balls __ball_active variable to True
    def activate_ball(self):
        self.ball_active = True
        #Set the balls direction to straight up
        self.direction = pygame.math.Vector2(0, -1).normalize()

    #Deactivate Ball Function sets the balls ball_active function to False and positions the ball at the center of the paddle
    def deactivate_ball(self, delta):
        self.ball_active = False
        paddle_pos = self.__paddle.get_pos
        paddle_width = self.__paddle.get_width
        #Set the balls x position to the center of the paddle
        self.position.x = paddle_pos + paddle_width / 2 - self.size / 2
        #Set the balls y position so that the bottom of the ball rests on the top of the paddle
        self.position.y = config.PADDLE_Y - self.size - 1

    #Reset Ball Function resets the ball to the middle of the paddle, and resets its direction vector to straight up
    def reset_ball(self):
        paddle_pos = self.__paddle.get_pos
        paddle_width = self.__paddle.get_width
        self.ball_speed = 0.5
        self.ball_active = False
        self.direction.x = 0
        self.direction.y = -1
        self.position.x = paddle_pos + paddle_width / 2 - self.size / 2
        self.position.y = config.PADDLE_Y - self.size - 1

    #Missed Ball Function
    #Missed Ball Function will check whether the ball has gone below the paddle and if so reset it, decrease its speed, and remove 1 life from lives left
    def missed_ball(self, delta):
        if self.ball_active == True:
            #Check if the balls position has gone below the top of the paddle
            if self.position.y > config.PADDLE_Y - self.size + (self.ball_speed * delta):
                #If the rapidball powerup is active, simple reverse the balls y direction
                if self.rapidball == True:
                    self.direction.y *= -1
                else:
                    return True

    #Increase Speed Function increases the balls ball_speed variable by 0.1
    def increase_speed(self):
        self.ball_speed += 0.1

    #Decrease Speed Function decreases the balls ball_speed variable by 0.05
    def decrease_speed(self):
        self.ball_speed -= 0.05

    #Reset Speed Function sets the ball speed back to 0.5
    def reset_speed(self):
        self.ball_speed = 0.5

    #Function Increase Size changes the image of the ball to the large ball
    def increase_size(self):
        self.img = config.BALL_IMGS['large_ball_img']

    #Function Reset Size resets the ball to its normal image and size
    def reset_size(self):
        self.img = config.BALL_IMGS['ball_img']

    #Function Decrease Size sets the ball to the small ball image and size
    def decrease_size(self):
        self.img = config.BALL_IMGS['small_ball_img']

    #Function Activate Nuclear sets the self.nuclear variable to True
    def activate_nuclear(self):
        self.nuclear = True

    #Function Deactivate Nuclear sets the self.nuclear variable to False
    def deactivate_nuclear(self):
        self.nuclear = False

    #Function Activate Rapid Ball sets the self.rapidball variable to true and sets the ball speed to 2
    def activate_rapid_ball(self):
        self.rapidball = True
        self.ball_speed = 2

    #Function Deactivate Rapid Ball sets self.rapidball to False and then calls the reset_ball method
    def deactivate_rapid_ball(self):
        self.rapidball = False
        self.reset_ball()

    #Function Activate Sticky Paddle sets the self.sticky_paddle variable to True
    def activate_sticky_paddle(self):
        self.sticky_paddle = True

    #Function Deactivate Sticky Paddle sets the self.sticky_paddle variable to True
    def deactivate_sticky_paddle(self):
        self.sticky_paddle = False

        
        

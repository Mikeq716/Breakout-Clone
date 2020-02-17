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

    #Update Function
    #Update function calculates new position and draws ball, checks for paddle collision and checks if ball is active
    def update(self, paddle, delta, scorecard):
        self.size = self.img.get_width()
        if self.ball_active == True:
            self.__move(delta)
        if self.ball_active == False:
            self.deactivate_ball(delta)

    #Function Move
    #Function Move reverses the balls direction if it hits a wall and calculates the balls movement for the current frame
    def __move(self, delta):        
        if self.position.x + self.size + self.direction.x * self.ball_speed * delta >= 800:
            self.direction.x *= -1
        if self.position.x + self.direction.x * self.ball_speed * delta <= 0:
            self.direction.x *= -1
        if self.position.y + self.direction.y * self.ball_speed * delta <= 35:
            self.direction.y *= -1            
        self.position += self.direction * self.ball_speed * delta
        
    #Function Draw
    #Function Draw blits the ball to the screen
    def draw(self, surface):
        surface.blit(self.img, self.position)

    #Function Spawn_Ball
    #Function Spawn_Ball will spawn a ball and add it to the list of balls
    def spawn_ball(ball_list, paddle):
        ball = Ball(paddle)
        if len(ball_list) > 0:
            ball.ball_active = True
        ball_list.append(ball)

    #Activate Ball Function
    #Activate Ball Function sets the balls __ball_active variable to True
    def activate_ball(self):
        self.ball_active = True

    #Deactivate Ball Function
    #Deactivate Ball Function checks whether the __ball_active variable is False, if so it moves the ball to the middle of the paddle each frame
    def deactivate_ball(self, delta):
        self.ball_active = False
        paddle_pos = self.__paddle.get_pos
        paddle_width = self.__paddle.get_width
        self.position.x = paddle_pos + paddle_width / 2 - self.size / 2
        self.position.y = config.PADDLE_Y - self.size - 1

    #Reset Ball Funtion
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
            if self.position.y > config.PADDLE_Y - self.size + (self.ball_speed * delta):
                if self.rapidball == True:
                    self.direction.y *= -1
                else:
                    return True

    #Increase Speed Function
    #Increase Speed Function increases the balls __ball_speed variable by 0.10
    def increase_speed(self):
        self.ball_speed += 0.05

    #Decrease Speed Function
    #Decrease Speed Function decreases the balls __ball_speed variable by 0.10
    def decrease_speed(self):
        self.ball_speed -= 0.05

    #Reset Speed Function
    #Reset Speed Function sets the ball speed back to 0.5
    def reset_speed(self):
        self.ball_speed = 0.5

    #Function Increase Size
    #Function Increase Size changes the image of the ball to the large ball
    def increase_size(self):
        self.img = config.BALL_IMGS['large_ball_img']

    #Function Decrease Size
    #Function Decrease Size resets the ball to its normal image and size
    def decrease_size(self):
        self.img = config.BALL_IMGS['ball_img']

    #Function Activate Nuclear
    #Function Activate Nuclear activates the nuclear powerup
    def activate_nuclear(self):
        self.nuclear = True

    #Function Deactivate Nuclear 
    #Function Deactivate Nuclear deactivates the nuclear powerup
    def deactivate_nuclear(self):
        self.nuclear = False

    #Function Activate Rapid Ball
    #Function Activate Rapid Ball activates the rapid ball powerup
    def activate_rapid_ball(self):
        self.rapidball = True
        self.ball_speed = 2

    #Function Deactivate Rapid Ball
    #Function Deactivate Rapid Ball deactivates the rapid ball powerup
    def deactivate_rapid_ball(self):
        self.rapidball = False
        self.ball_speed = 0.5
        self.reset_ball()

    #Function Activate Sticky Paddle
    #Function Activate Sticky Paddle activates the sticky paddle powerup
    def activate_sticky_paddle(self):
        self.sticky_paddle = True

    #Function Deactivate Sticky Paddle
    #Function Deactivate Sticky Paddle deactivates the sticky paddle powerup
    def deactivate_sticky_paddle(self):
        self.sticky_paddle = False

        
        

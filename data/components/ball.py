import pygame

from .. import config

#Ball class definition
class Ball:
    def __init__(self, paddle):
        self.__img = config.BALL_IMGS['ball_img']
        self.__size = self.__img.get_width()
        self.__position = pygame.math.Vector2(paddle.get_pos + paddle.get_width / 2 + self.__size / 2)
        self.__direction = pygame.math.Vector2(0, -1).normalize()
        self.__ball_active = False
        self.__ball_speed = 0.5
        self.__nuclear = False
        self.__rapidball = False
        self.__paddle = paddle

    #Update Function
    #Update function calculates new position and draws ball, checks for paddle collision and checks if ball is active
    def update(self, ball, delta, scorecard):
        self.__size = self.__img.get_width()
        self.__move(delta)
        self.__check_paddle_collision(delta)
        if self.__ball_active == False:
            self.__inactive_ball(delta)

    #Function Draw
    #Function Draw blits the ball to the screen
    def draw(self, surface):
        surface.blit(self.__img, self.__position)

    #Activate Ball Function
    #Activate Ball Function sets the balls __ball_active variable to True
    def activate_ball(self):
        self.__ball_active = True

    #Reset Ball Funtion
    #Reset Ball Function resets the ball to the middle of the paddle, and resets its direction vector to straight up
    def reset_ball(self):
        paddle_pos = self.__paddle.get_pos
        paddle_width = self.__paddle.get_width
        self.__ball_active = False
        self.__direction.x = 0
        self.__direction.y = 1
        self.__position.x = paddle_pos + paddle_width / 2 - self.__size / 2
        self.__position.y = config.PADDLE_Y - self.__size - 1

    #Increase Speed Function
    #Increase Speed Function increases the balls __ball_speed variable by 0.10
    def increase_speed(self):
        self.__ball_speed += 0.05

    #Decrease Speed Function
    #Decrease Speed Function decreases the balls __ball_speed variable by 0.10
    def decrease_speed(self):
        self.__ball_speed -= 0.05

    #Reset Speed Function
    #Reset Speed Function sets the ball speed back to 0.5
    def reset_speed(self):
        self.__ball_speed = 0.5

    #Function Increase Size
    #Function Increase Size changes the image of the ball to the large ball
    def increase_size(self):
        self.__img = config.BALL_IMGS['large_ball_img']

    #Function Decrease Size
    #Function Decrease Size resets the ball to its normal image and size
    def decrease_size(self):
        self.__img = config.BALL_IMGS['ball_img']

    #Function Activate Nuclear
    #Function Activate Nuclear activates the nuclear powerup
    def activate_nuclear(self):
        self.__nuclear = True

    #Function Deactivate Nuclear 
    #Function Deactivate Nuclear deactivates the nuclear powerup
    def deactivate_nuclear(self):
        self.__nuclear = False

    #Function Activate Rapid Ball
    #Function Activate Rapid Ball activates the rapid ball powerup
    def activate_rapid_ball(self):
        self.__rapidball = True
        self.__ball_speed = 2.5

    #Function Deactivate Rapid Ball
    #Function Deactivate Rapid Ball deactivates the rapid ball powerup
    def deactivate_rapid_ball(self):
        self.__rapidball = False
        self.__ball_speed = 0.5
        self.reset_ball()

    #Check Brick Collision Function
    #Check Brick Collision Function checks if ball has collided with brick and if it has it reverses balls direction on the correct axis and returns true
    def check_brick_collision(self, ball, brick, delta):
        check_x = self.__position.x
        check_y = self.__position.y
        brick_pos = brick.get_pos
        if check_x > brick_pos.x and check_x < brick_pos.x + config.BRICK_WIDTH: 
            if check_y < brick_pos.y + config.BRICK_HEIGHT and check_y > brick_pos.y + config.BRICK_HEIGHT - (self.__ball_speed * delta) and self.__direction.y < 0:
                if self.__nuclear == False:    
                    self.__direction.y *= -1
                return True
        if check_x > brick_pos.x and check_x < brick_pos.x + config.BRICK_WIDTH:
            if check_y + self.__size > brick_pos.y and check_y < brick_pos.y + (self.__ball_speed * delta) and self.__direction.y > 0:
                if self.__nuclear == False:
                    self.__direction.y *= -1
                return True
        if check_y > brick_pos.y and check_y < brick_pos.y + config.BRICK_HEIGHT:
            if check_x + self.__size > brick_pos.x and check_x < brick_pos.x + (self.__ball_speed * delta) and self.__direction.x > 0:
                if self.__nuclear == False:
                    self.__direction.x *= -1
                return True
        if check_y > brick_pos.y and check_y < brick_pos.y + config.BRICK_HEIGHT:
            if check_x < brick_pos.x + config.BRICK_WIDTH and check_x > brick_pos.x + config.BRICK_WIDTH - (self.__ball_speed * delta) and self.__direction.x < 0:
                if self.__nuclear == False:
                    self.__direction.x *= -1
                return True

    #Missed Ball Function
    #Missed Ball Function will check whether the ball has gone below the paddle and if so reset it, decrease its speed, and remove 1 life from lives left
    def missed_ball(self, delta):
        if self.__position.y > config.PADDLE_Y - self.__size + (self.__ball_speed * delta):
            if self.__rapidball == True:
                self.__direction.y *= -1
            else:
                return True

    #Inactive Ball Function
    #Inactive Ball Function checks whether the __ball_active variable is False, if so it moves the ball to the middle of the paddle each frame
    def __inactive_ball(self, delta):
        paddle_pos = self.__paddle.get_pos
        paddle_width = self.__paddle.get_width
        self.__position.x = paddle_pos + paddle_width / 2 - self.__size / 2
        self.__position.y = config.PADDLE_Y - self.__size - 1

    #Check Paddle Collision Function
    #Check Paddle Collision Function checks if ball has collided with the paddle and returns true if it has
    #Check Paddle Collision Function calculates and sets the balls correct bounce angle depending on where on the paddle the collision happened
    def __check_paddle_collision(self, delta):
        paddle_pos = self.__paddle.get_pos
        paddle_width = self.__paddle.get_width
        check_pos_x = self.__position.x + (self.__size / 2) + self.__direction.x * self.__ball_speed * delta
        check_pos_y = self.__position.y + self.__size + self.__direction.y * self.__ball_speed * delta
        paddle_split_pos = paddle_pos + (paddle_width / 2)
        y_vel = self.__direction.y
        if check_pos_y >= config.PADDLE_Y:
            if check_pos_x >= paddle_pos and check_pos_x <= paddle_pos + paddle_width:
                if check_pos_x < paddle_split_pos:
                    ball_dist = paddle_split_pos - check_pos_x
                    x_vel = ball_dist / (paddle_width / 2) * -1
                    self.__direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()
                if check_pos_x > paddle_split_pos:
                    ball_dist = check_pos_x - paddle_split_pos
                    x_vel = ball_dist / (paddle_width / 2)
                    self.__direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()

    #Function Move
    #Function Move reverses the balls direction if it hits a wall and calculates the balls movement for the current frame
    def __move(self, delta):        
        if self.__position.x + self.__size + self.__direction.x * self.__ball_speed * delta >= 800:
            self.__direction.x *= -1
        if self.__position.x + self.__direction.x * self.__ball_speed * delta <= 0:
            self.__direction.x *= -1
        if self.__position.y + self.__direction.y * self.__ball_speed * delta <= 35:
            self.__direction.y *= -1            
        self.__position += self.__direction * self.__ball_speed * delta
        
        

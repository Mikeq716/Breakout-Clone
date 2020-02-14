import pygame
import random

from .. import config

class Powerup:
    def __init__(self, pos, img):
        self.position = pygame.math.Vector2(pos)
        self.velocity = pygame.math.Vector2(random.randint(-1, 1), 2).normalize()
        self.width = config.POWERUP_IMGS['powerup_health_img'].get_width()
        self.img = img
        self.timer = 0
        self.activated = False

    #Function Spawn Powerup
    #Function Spawn Powerup decides whether to spawn a powerup and if one is to be spawned, it is added to the spawned powerups list
    def spawn_powerup(spawned_list, pos):
        if random.randint(1, 10) == 1:
            pu = random.randint(1, 10)
            spawned_list.append(POWERUPS[pu](pos, PU_IMG[pu]))

    #Function Update
    #Function Update moves the spawned powerup, checks if it collided with the paddle, and deletes it if it drops below the paddle
    #Function Update also draws the powerup onto the screen
    def update_spawned_powerups(self, delta, spawned_list, activated_list, paddle):
        self.move(delta)
        self.check_activated(spawned_list, activated_list, paddle)
        if self.position.y > config.PADDLE_Y:
            self.delete(spawned_list)

    #Function Check Activated
    #Function Check Activated checks if the spawned powerup collides with the paddle, and if it does it activates the powerup
    def check_activated(self, spawned_list, activated_list, paddle):
        paddle_pos = paddle.get_pos
        paddle_width = paddle.get_width
        if self.position.y + config.POWERUP_IMGS['powerup_health_img'].get_height() >= config.PADDLE_Y and self.position.y <= config.PADDLE_Y:
            if self.position.x + self.width > paddle_pos and self.position.x < paddle_pos + paddle_width:
               activated_list.append(self) 
               self.delete(spawned_list)
    
    #Function Draw
    #Function draw blits the spawned powerup to the screen
    def draw(self, surface):
        surface.blit(self.img, self.position)

    #Function Move
    #Function Move reverses the spawned powerups x velocity if it hits a wall and calculates its new position on the screen for the current frame
    def move(self, delta):
        self.position += self.velocity * delta * 0.25
        if self.position.x <= 0:
            self.velocity.x *= -1
        elif self.position.x + config.POWERUP_IMGS['powerup_health_img'].get_width() >= config.SCREEN_WIDTH:
            self.velocity.x *= -1

    #Function Delete
    #Function Delete removes the spawned powerup from the list of spawned powerups
    def delete(self, pu_list):
        pu_list.remove(self)


class HealthPowerup(Powerup):
    #Function Activate
    #Function Activate for the Health powerup adds a life to the current lives, and then deletes itself
    def activate(self, paddle, ball, scorecard):
        scorecard.add_life()
        self.activated = True

    #Function Update
    #Function Update for the Health powerup simply deletes it from the activated list
    def update(self, activated_list, paddle, ball, scorecard, delta):
        self.delete(activated_list)


class HealthDecrease(Powerup):
    #Function Activate
    #Function Activate removes a life from the current lives unless there is only 1 life left
    def activate(self, paddle, ball, scorecard):
        if scorecard.lives_left > 1:
            scorecard.remove_life()
        self.activated = True

    #Function Update
    #Function Update for the HealthDecrease powerup simply deletes it from the activated list
    def update(self, activated_list, paddle, ball, scorecard, delta):
        self.delete(activated_list)


class IncreasePaddleSize(Powerup):
    #Function Activate
    #Function Activate for the IncreasePaddleSize powerup increases the paddles size if its not at maximum and then deletes itself
    def activate(self, paddle, ball, scorecard):
        paddle.increase_paddle_size()
        self.activated = True

    def update(self, activated_list, paddle, ball, scorecard, delta):
        self.timer += delta
        if self.timer >= 10000:
            self.deactivate(paddle, ball)
            self.delete(activated_list)

    def deactivate(self, paddle, ball):
        paddle.reset_paddle_size()


class DecreasePaddleSize(Powerup):
    #Function Activate
    #Function Activate for the DecreasePaddleSize powerup decreases the paddles size if its not at minimum and then deletes itself
    def activate(self, paddle, ball, scorecard):
        paddle.decrease_paddle_size()
        self.activated = True

    def update(self, activated_list, paddle, ball, scorecard, delta):
        self.timer += delta
        if self.timer >= 10000:
            self.deactivate(paddle, ball)
            self.delete(activated_list)

    def deactivate(self, paddle, ball):
        paddle.reset_paddle_size()


class IncreaseBallSpeed(Powerup):
    #Function Activate
    #Function Activate for the IncreaseBallSpeed powerup increases the balls speed
    def activate(self, paddle, ball, scorecard):
        ball.increase_speed()
        self.activated = True

    def update(self, activated_list, paddle, ball, scorecard, delta):
        self.timer += delta
        if self.timer >= 10000:
            self.deactivate(paddle, ball)
            self.delete(activated_list)

    def deactivate(self, paddle, ball):
        ball.decrease_speed()


class DecreaseBallSpeed(Powerup):
    #Function Activate
    #Function Activate for the DecreaseBallSpeed powerup decreases the balls speed
    def activate(self, paddle, ball, scorecard):
        ball.decrease_speed()
        self.activated = True

    def update(self, activated_list, paddle, ball, scorecard, delta):
        self.timer += delta
        if self.timer >= 10000:
            self.deactivate(paddle, ball)
            self.delete(activated_list)

    def deactivate(self, paddle, ball):
        ball.increase_speed()        


class IncreaseBallSize(Powerup):
    #Function Activate
    #Function Activate for the IncreaseBallSize powerup increases the size of the ball
    def activate(self, paddle, ball, scorecard):
        ball.increase_size()
        self.activated = True

    def update(self, activated_list, paddle, ball, scorecard, delta):
        self.timer += delta
        if self.timer >= 10000:
            self.deactivate(paddle, ball)
            self.delete(activated_list)

    def deactivate(self, paddle, ball):
        ball.decrease_size()


class NuclearBall(Powerup):
    #Function Activate
    #Function Activate for the NuclearBall powerup makes the ball continue straight through bricks it has destroyed
    def activate(self, paddle, ball, scorecard):
        ball.activate_nuclear()
        self.activated = True

    def update(self, activated_list, paddle, ball, scorecard, delta):
        self.timer += delta
        if self.timer >= 5000:
            self.deactivate(paddle, ball)
            self.delete(activated_list)

    def deactivate(self, paddle, ball):
        ball.deactivate_nuclear()


class HideBricks(Powerup):
    #Function Activate
    #Function Activate for the HideBricks powerup sets the HIDE_BRICKS variable in config to true
    def activate(self, paddle, ball, scorecard):
        config.HIDE_BRICKS = True
        self.activated = True

    def update(self, activated_list, paddle, ball, scorecard, delta):
        self.timer += delta
        if self.timer >= 10000:
            self.deactivate(paddle, ball)
            self.delete(activated_list)

    def deactivate(self, paddle, ball):
        config.HIDE_BRICKS = False


class RapidBall(Powerup):
    #Function Activate
    #Function Activate for the RapidBall powerup calls the activate_rapid_ball function of the ball
    def activate(self, paddle, ball, scorecard):
        ball.activate_rapid_ball()
        self.activated = True

    def update(self, activated_list, paddle, ball, scorecard, delta):
        self.timer += delta
        if self.timer >= 3000:
            self.deactivate(paddle, ball)
            self.delete(activated_list)

    def deactivate(self, paddle, ball):
        ball.deactivate_rapid_ball()

   
POWERUPS = {1 : HealthPowerup, 
            2 : IncreasePaddleSize, 
            3 : DecreasePaddleSize,
            4 : IncreaseBallSpeed,
            5 : DecreaseBallSpeed,
            6 : IncreaseBallSize,
            7 : NuclearBall,
            8 : HealthDecrease,
            9 : HideBricks,
            10 : RapidBall
}

PU_IMG = {  1 : config.POWERUP_IMGS['powerup_health_img'],
            2 : config.POWERUP_IMGS['powerup_increase_paddle_img'], 
            3 : config.POWERUP_IMGS['powerup_decrease_paddle_img'],
            4 : config.POWERUP_IMGS['powerup_increase_ball_speed_img'],
            5 : config.POWERUP_IMGS['powerup_decrease_ball_speed_img'], 
            6 : config.POWERUP_IMGS['powerup_increase_ball_size_img'],
            7 : config.POWERUP_IMGS['powerup_nuclear_ball_img'],
            8 : config.POWERUP_IMGS['powerup_health_decrease_img'],
            9 : config.POWERUP_IMGS['powerup_hide_bricks_img'],
            10 : config.POWERUP_IMGS['powerup_rapid_ball_img']
}
            
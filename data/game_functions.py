import pygame

from . import config
from .components.powerup import Powerup
from .components.level import Level

class GameFunctions:
    #New Game Function
    #New Game Function resets everything and starts a new game
    def new_game(game):
        config.CURRENT_COUNT = 0
        game.new = False
        game.bricks.clear()
        game.current_level = 0
        game.scorecard.lives_left = 3
        game.scorecard.current_score = 0
        game.paddle.reset_paddle_size()
        GameFunctions.clear_powerups(game)
        for ball in game.ball_list:
            ball.reset_ball()

    #Check Brick Collision Function
    #Check Brick Collision Function checks if ball has collided with brick and if it has it reverses balls direction on the correct axis and returns true
    def check_brick_collision(ball, brick, delta):
        ball_pos = ball.position
        ball_size = ball.size
        ball_speed = ball.ball_speed
        ball_direction = ball.direction
        brick_pos = brick.get_pos

        if ball_pos.x > brick_pos.x and ball_pos.x < brick_pos.x + config.BRICK_WIDTH: 
            if ball_pos.y < brick_pos.y + config.BRICK_HEIGHT and ball_pos.y > brick_pos.y + config.BRICK_HEIGHT - (ball_speed * delta) and ball_direction.y < 0:
                if ball.nuclear == False:    
                    ball_direction.y *= -1
                return True
        if ball_pos.x > brick_pos.x and ball_pos.x < brick_pos.x + config.BRICK_WIDTH:
            if ball_pos.y + ball_size > brick_pos.y and ball_pos.y < brick_pos.y + (ball_speed * delta) and ball_direction.y > 0:
                if ball.nuclear == False:
                    ball_direction.y *= -1
                return True
        if ball_pos.y > brick_pos.y and ball_pos.y < brick_pos.y + config.BRICK_HEIGHT:
            if ball_pos.x + ball_size > brick_pos.x and ball_pos.x < brick_pos.x + (ball_speed * delta) and ball_direction.x > 0:
                if ball.nuclear == False:
                    ball_direction.x *= -1
                return True
        if ball_pos.y > brick_pos.y and ball_pos.y < brick_pos.y + config.BRICK_HEIGHT:
            if ball_pos.x < brick_pos.x + config.BRICK_WIDTH and ball_pos.x > brick_pos.x + config.BRICK_WIDTH - (ball_speed * delta) and ball_direction.x < 0:
                if ball.nuclear == False:
                    ball_direction.x *= -1
                return True


    #Check Paddle Collision Function
    #Check Paddle Collision Function checks if ball has collided with the paddle and returns true if it has
    #Check Paddle Collision Function calculates and sets the balls correct bounce angle depending on where on the paddle the collision happened
    def check_paddle_collision(ball, paddle, delta):
        paddle_pos = paddle.get_pos
        paddle_width = paddle.get_width
        paddle_split_pos = paddle_pos + (paddle_width / 2)
        check_pos_x = ball.position.x + ball.direction.x * ball.ball_speed * delta
        check_pos_y = ball.position.y + ball.size + ball.direction.y * ball.ball_speed * delta
        y_vel = ball.direction.y

        if check_pos_y >= config.PADDLE_Y:
            if check_pos_x <= paddle_pos + paddle_width and check_pos_x + ball.size >= paddle_pos:
                if ball.sticky_paddle == True:
                    ball.deactivate_ball(delta)
                if check_pos_x < paddle_split_pos:
                    ball_dist = paddle_split_pos - check_pos_x
                    x_vel = ball_dist / (paddle_width / 2) * -1
                    ball.direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()
                if check_pos_x > paddle_split_pos:
                    ball_dist = check_pos_x - paddle_split_pos
                    x_vel = ball_dist / (paddle_width / 2)
                    ball.direction = pygame.math.Vector2(x_vel, y_vel * -1).normalize()

    #Update Level Function
    #Update Level Function will check if any bricks were hit, and if they were it will remove them
    def update_level(game):
        for row in game.bricks:
            if len(row) == 0:
                game.bricks.remove(row)
            for brick in row:
                brick.move(game.delta)
                for ball in game.ball_list:
                    if GameFunctions.check_brick_collision(ball, brick, game.delta) == True: 
                        game.scorecard.add_score(brick.get_value)
                        if brick.locked == False:
                            Powerup.spawn_powerup(game.spawned_powerups, brick.get_pos)
                            row.remove(brick)
                            config.CURRENT_COUNT -= 1
                        break

     #Next Level Function
    #Next Level Function loads the next level
    def next_level(game):
        Level.new_level(game.current_level, game.bricks)
        game.current_level += 1
        game.paddle.reset_paddle_size()
        GameFunctions.clear_powerups(game)
        for ball in game.ball_list:
            ball.reset_ball()
            ball.increase_speed()

    #Update Powerups Function
    #Update Powerups Function will update both spawned an activated powerups
    def update_powerups(game):
        for powerup in game.spawned_powerups:
            powerup.update_spawned_powerups(game.delta, game.spawned_powerups, game.activated_powerups, game.paddle)  
        for powerup in game.activated_powerups:
            if powerup.activated == False:
                powerup.activate(game.paddle, game.ball_list, game.scorecard)
            if powerup.activated == True:
                powerup.update(game.activated_powerups, game.paddle, game.ball_list, game.scorecard, game.delta)

    #Clear Powerups Function
    #Clear Powerups Function will deactivate all active powerups, and delete all spawned powerups
    def clear_powerups(game):
        for powerup in game.activated_powerups:
            powerup.deactivate(game.paddle, game.ball_list)
        game.activated_powerups.clear()
        game.spawned_powerups.clear()

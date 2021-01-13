import pygame
from pygame.locals import *
import sys, os
import time
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((400,600), 0, 32)

frog_rect = pygame.Rect(100,200, 32, 32)


moving_left = False
moving_right = False


running = True
falling = True
jumping = False
vertical_momentum = 0

frog_y_check = 0
balls = []
y_check = frog_rect.y

jumping = pygame.image.load("jumping.png")
jumping = pygame.transform.scale(jumping, (64, 64))
idle = pygame.image.load("idle.png")
idle = pygame.transform.scale(idle, (64, 64))

ball_img = pygame.image.load("ball.png")
ball_img = pygame.transform.scale(ball_img, (60,60))
ball_count = 2


### Here is where all of the ball values are set ###aaa 
ball_vel = random.randint(2, 3)
ball_spawn = [[399, 599, [-1.5, -1.5], [-1.5, -0.5]],[199,1, [1, 1.5], [1.3, 2.5]], [99,1, [0.3, 2], [0.1, 1]], [1,349, [2.5, -1], [2.5, -2.3]], [1,599, [1, -2.5], [1, -3.4]]]
random_spawn = random.randint(0, len(ball_spawn)-1)

"""
The current plan is to make a list of ball coordinates and possible velocities (which will be randomlly picked). 
Then before the loop I will create a rect which will constantly be updated to an x and y variable gotten from the list.
"""
balls = []
for x in range(len(ball_spawn)-1):
    random_vel = random.randint(2, 3)
    ball = [ball_spawn[x][0], ball_spawn[x][1], ball_spawn[x][random_vel][0], ball_spawn[x][random_vel][1]]
    balls.append(ball)

visible_balls = []

### Generate the ball list here ###
for _ in range(len(balls)-1):
    random_ball = random.randint(0, len(balls)-1)
    newball = balls[random_ball]
    visible_balls.append(newball)


while running:
    screen.fill((255, 255, 255))
    
    velocity = [0,0]
    if frog_rect.y > 500:
        vertical_momentum = 0
        velocity[1] = 0
        frog_rect.y = 500

     ##### Simulates Gravity #####
    if frog_rect.y < 550:
        vertical_momentum += 0.1
    velocity[1] += vertical_momentum

    if y_check < frog_rect.y:
        action = idle
    elif y_check > frog_rect.y:
        action = jumping
    elif y_check == frog_rect.y:
        action = idle
    y_check = frog_rect.y
    
    screen.blit(action, (frog_rect.x, frog_rect.y))


    for index, ball in enumerate(visible_balls):
        if ball[0] > 0 and ball[0] < 400 and ball[1] > 0 and ball[1] < 600: 
            ball_rect = pygame.Rect(ball[0], ball[1], 20, 20)
            screen.blit(ball_img, (ball[0], ball[1]))
            ball[0] += ball[2]
            ball[1] += ball[3]
        else:
            visible_balls.remove(ball)
            print("removed: ", ball)
            newball = balls[random.randint(0, len(balls)-1)]
            print(ball)
            visible_balls.append(newball)
            print("appended: ", newball)

    ##### movement function here #####
    if moving_left == True:  
        velocity[0] -= 1.5
    if moving_right == True:
        velocity[0] += 2
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                vertical_momentum = -5
                
        if event.type == KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    frog_rect.x += velocity[0]
    frog_rect.y += velocity[1]            
    pygame.display.update()
    clock.tick(120)

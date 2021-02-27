import pygame
from pygame.locals import *
import sys, os
import time
import random

pygame.init()
clock = pygame.time.Clock()

screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

frog_rect = pygame.Rect(100,200, 32, 32)

moving_left = False
moving_right = False

running = True
falling = True
jumping = False
vertical_momentum = 0

frog_y_check = 0
rocks = []
y_check = frog_rect.y

########### LOADING IMAGES ###########
jumping_img_load  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jumping.png")
jumping = pygame.image.load(jumping_img_load).convert()
jumping.set_colorkey((255, 255, 255))
jumping = pygame.transform.scale(jumping, (64, 64))

d_img_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "d.png")
d_img = pygame.image.load(d_img_load)
d_img = pygame.transform.scale(d_img, (100, 100))
e_img_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "e.png")
e_img = pygame.image.load(e_img_load)
e_img = pygame.transform.scale(e_img, (100, 100))
a_img_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a.png")
a_img = pygame.image.load(a_img_load)
a_img = pygame.transform.scale(a_img, (100, 100))

idle_image_load  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "idle.png")
idle = pygame.image.load(idle_image_load).convert()
idle.set_colorkey((255, 255, 255))
idle = pygame.transform.scale(idle, (64, 64))


rock_img_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ball.png")
rock_img = pygame.image.load(rock_img_load)
rock_img = pygame.transform.scale(rock_img, (60,60))
rock_count = 2

### Here i need to add the system where the rocks are randomly generated and made into an actual pieve of data ###
def ran(x, y):
    rand = random.randint(x, y)
    return ran(x, y) if rand == 0 else rand

top_rect = pygame.Rect(0, -25, 400, 1)
bottom_rect = pygame.Rect(0, 625, 400, 1)
left_rect = pygame.Rect(-20, 0, 1, 600)
right_rect = pygame.Rect(420, 1, 1, 600)

data = []

def make_int(val):
    if val < 0:
        val = int(val+0.5)
    elif val > 0:
        val = int(val-0.5)
    return val

def generate_new():
    ran_x = random.randint(20, screen_width-10)
    ran_y = random.randint(10, 100)

    x_vel = ran(-1, 1)
    y_vel = ran(1, 3)
    ##makes the vels ints###
    v_vel = make_int(x_vel)
    y_vel = make_int(y_vel)
    if y_vel == 0:
        y_vel = random.randint(1, 2)
    return ran_x, ran_y, x_vel, y_vel

for x in range(3):
    ran_x, ran_y, x_vel, y_vel = generate_new()
    data.append([ran_x, ran_y, x_vel, y_vel])

game_over = False
running = True
fill = (0, 235, 155)
while True:
    screen.fill(fill)

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

    if running:
        screen.blit(action, (frog_rect.x, frog_rect.y))

    ##### movement function here #####
    if moving_left == True:
        velocity[0] -= 1.5
    if moving_right == True:
        velocity[0] += 2

    for x in data:
        if running:
            rect = pygame.Rect(x[0], x[1], rock_img.get_width(), rock_img.get_height())
            screen.blit(rock_img, (x[0], x[1]))

            #if (rect.x < 0) or (rect.x > screen_width) or (rect.y < 0) or (rect.y > screen_height):

            if rect.colliderect(bottom_rect) or rect.colliderect(top_rect) or rect.colliderect(left_rect) or rect.colliderect(right_rect):
                ran_x, ran_y, x_vel, y_vel = generate_new()
                x[0] = ran_x
                x[1] = ran_y
                x[2] = x_vel
                x[3] = y_vel
                ran_x, ran_y, x_vel, y_vel = generate_new()

                #Unhash the line below if you want to see shit go down
                #data.append([ran_x, ran_y, x_vel, y_vel])


            if (rect.x > 0) or (rect.x < screen_width) or (rect.y > 0) or (rect.y < screen_height):
                x[0] += int(x[2])
                x[1] += int(x[3])

        if frog_rect.colliderect(rect):
            fill = (0, 0, 0)
            running = False
            ### blit ending screen ###
            game_over = True

    if game_over:
        screen.blit(d_img, (0, 250))
        screen.blit(e_img, (100, 250))
        screen.blit(a_img, (200, 250))
        screen.blit(d_img, (300, 250))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
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

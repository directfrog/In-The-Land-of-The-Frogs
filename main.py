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

rock_index = 0

def append_rocks():
    global rock_index
    random_choice = random.randint(1, 2)
    if random_choice == 1:
        x = random.randint(0, screen_width)
        y = 0
        if x > screen_width/2:
            vel = [ran(-1, 3), ran(1, 3)]
        elif x < screen_width/2:
            vel = [ran(-1, 3), ran(1, 3)]
    if random_choice == 2:
        x = 0
        y = ran(0, screen_height)
        if y > screen_height/2:
            vel = [ran(1, 3), ran(1, 3)]
        elif y < screen_height/2:
            vel = [ran(1, 3), ran(-3, -1)]
    rock = [x, y, vel, rock_index]
    rock_index += 1
    return rock

top_rect = pygame.Rect(0, -25, 400, 1)
bottom_rect = pygame.Rect(0, 625, 400, 1)
left_rect = pygame.Rect(-20, 0, 1, 600)
right_rect = pygame.Rect(420, 1, 1, 600)

data = []

for x in range(3):
    new_rock = data.append(append_rocks())


while running:
    screen.fill((0, 235, 155))

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

    ##### movement function here #####
    if moving_left == True:
        velocity[0] -= 1.5
    if moving_right == True:
        velocity[0] += 2

    for x in data:
        rect = pygame.Rect(x[0], x[1], rock_img.get_width(), rock_img.get_height())
        screen.blit(rock_img, (rect.x, rect.y))
        x[0] += x[2][0]
        x[1] += x[2][1]

        if rect.colliderect(top_rect) or rect.colliderect(bottom_rect) or rect.colliderect(left_rect) or rect.colliderect(right_rect):
            '''
            try:
                data.remove(data[x[3]])
            except:
                print(data)
                print(x)
            '''
            print(rock_index)
            new_rock = append_rocks()
            data.append(new_rock)

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

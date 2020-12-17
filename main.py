import pygame
from pygame.locals import *
import sys, os
import time

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((300,600), 0, 32)
display = pygame.Surface((200,600))

frog_rect = pygame.Rect(100,200, 16, 16)

    

frog2 = pygame.image.load("animations/idle animations/frog2.gif")


moving_left = False
moving_right = False

running = True
falling = True

while running:
    screen.fill((255, 255, 255))

    screen.blit(frog2, (frog_rect.x, frog_rect.y))

    
    velocity = [0,0]

    ##### Adds inpenetratable floor #####
    if frog_rect.y > 580:
        velocity[1] = 0
        frog_rect.y = 580

    ##### Simulates Gravity #####
    if falling == True:
        if frog_rect.y < 580:
            frog_rect.y += 2

    ##### movement function here #####
    if moving_left == True:
        velocity[0] -= 1.5
    if moving_right == True:
        velocity[0] += 2


    frog_rect.x += velocity[0]
    frog_rect.y -= velocity[1]

    
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
                falling = False
                velocity[1] += 5
        if event.type == KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    print(frog_rect.y)
            

    pygame.display.update()
    clock.tick(120)

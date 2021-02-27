import pygame
from pygame.locals import *
import sys, os
import time
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400,600), 0, 32)

ball_spawn = [[400, 600, [-1.5, -1.5], [-1.5, -0.5]],[200,0, [0, 1.5], [0.3, 2.5]], [100,0, [0.3, 2], [0.1, 1]], [0,350, [2.5, -1], [2.5, -2.3]], [0,600, [1, -2.5], [2, 1.4]]]

balls = []
for x in range(len(ball_spawn)):
    random_vel = random.randint(2, 3)
    #This adds each ball
    balls.append([ball_spawn[x][0], ball_spawn[x][1], ball_spawn[x][random_vel][0], ball_spawn[x][random_vel][1]])



for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    if event.type == KEYDOWN:
       	if event.key == ESCAPE:
        	pygame.quit()
        	sys.exit()
import pygame
from pygame.locals import *
import random
pygame.init()
clock = pygame.time.Clock()
import sys

screen = pygame.display.set_mode((400, 600), 0, 32)
rock_img = pygame.image.load("ball.png")
rock_img = pygame.transform.scale(rock_img, (80, 80))

rock_vel = random.randint(2, 3)
rock_spawn = [[399, 599, [-1.5, -1.5], [-1.5, -0.5]],[199,1, [1, 1.5], [1.3, 2.5]], [99,1, [0.3, 2], [0.1, 1]], [1,349, [2.5, -1], [2.5, -2.3]], [1,599, [1, -2.5], [1, -3.4]]]
random_spawn = random.randint(0, len(rock_spawn)-1)

def ran_loop(v_rocks, rocks):
	for x in range(0, 3):
		ran = random.randint(0, len(rocks)-1)
		if rocks[ran] not in v_rocks:
			v_rocks.append(rocks[ran])
		

rocks = []
for x in range(len(rock_spawn)):
    random_vel = random.randint(2, 3)
    rock = [rock_spawn[x][0], rock_spawn[x][1], rock_spawn[x][random_vel][0], rock_spawn[x][random_vel][1], f"name=rock{x}"]
    rocks.append(rock)

visible_rocks = []
for x in range(3):
	ran = random.randint(0, len(rocks)-1)
	if rocks[ran] not in visible_rocks:
		visible_rocks.append(rocks[ran])
	else:
		ran_loop(visible_rocks, rocks)

print(visible_rocks)

running = True
while running:
	screen.fill((255, 255, 255))

	for x in visible_rocks:
		rect = pygame.Rect(x[0], x[1], 20, 20)
		screen.blit(rock_img, (x[0], x[1]))
		x[0] += x[2]/5
		x[1] += x[3]/5

		if x[0] < 0 or x[0] > 400 or x[1] < 0 or x[1] > 600:
			visible_rocks.remove(visible_rocks[x])
			for x in range(0, random.randint(1, 3)):
				ran_loop(visible_rocks, rocks)


	print(visible_rocks)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
	pygame.display.update()
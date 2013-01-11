#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

pygame.mouse.set_visible(0)

ship = pygame.image.load("images/SHIP.png")


shootnumx = 0
shootnumy = 0
shoot_y = screen.get_height()/2
shoot_x = screen.get_width()/2

while True:
	clock.tick(60)
	screen.fill((255,255,255))

	screen.blit(ship, (shoot_x, shoot_y))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			sys.exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			shootnumy = 5
		elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
			shootnumy = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			shootnumy = -5
		elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			shootnumy = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			shootnumx = 5
		elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
			shootnumx = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			shootnumx = -5
		elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
			shootnumx = 0
	if shoot_y != 0 or shoot_x != 0:
		screen.blit(ship, (shoot_x, shoot_y))
		shoot_y -= shootnumy
		shoot_x -= shootnumx
	pygame.display.update()

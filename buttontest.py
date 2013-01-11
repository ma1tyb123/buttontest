#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1080,720))

pygame.mouse.set_visible(0)

ship = pygame.image.load("images/SHIP.png")


speed = 0
shipupdate_x = 0
shipupdate_y = 0
center_x = screen.get_width()/2 - ship.get_width()/2
center_y = screen.get_height()/2 - ship.get_height()/2
ship_y = center_y
ship_x = center_x
firstspeed = 0
checkcenter = 0
while True:
	clock.tick(60)
	screen.fill((255,255,255))
	screen.blit(ship, (ship_x, ship_y))
	if firstspeed == 0:
		speed = 5
		firstspeed = 1
	if checkcenter == 0:
		center_x = screen.get_width()/2 - ship.get_width()/2
		center_y = screen.get_height()/2 - ship.get_height()/2
		checkcenter = 1
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			sys.exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
			screen.blit(ship, (ship_x, ship_y))
			ship_y = center_y
			ship_x = center_x
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
			speed = 5
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
			speed = 10
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
			speed = 15
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
			speed = 20
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			shipupdate_y = speed
		elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
			shipupdate_y = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			shipupdate_y = -speed
		elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			shipupdate_y = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			shipupdate_x = speed
		elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
			shipupdate_x = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			shipupdate_x = -speed
		elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
			shipupdate_x = 0
	if ship_y != 0 or ship_x != 0:
		screen.blit(ship, (ship_x, ship_y))
		ship_y -= shipupdate_y
		ship_x -= shipupdate_x
	pygame.display.update()

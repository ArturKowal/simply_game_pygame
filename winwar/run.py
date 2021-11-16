import pygame
from pygame import Vector2
import sys

pygame.init()
screen=pygame.display.set_mode((1280,720)) #1280,720
box=[10,10,50,50]
clock=pygame.time.Clock()
delta=0.0

while True:
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
		if event.type ==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
			sys.exit(0)

	#Ticking
	delta+=clock.tick()/1000.0
	

	#Input
	keys=pygame.key.get_pressed()
	if keys[pygame.K_d]:
		box[0]+=1
	if keys[pygame.K_s]:
		box[1]+=1
	if keys[pygame.K_a]:
		box[0]-=1
	if keys[pygame.K_w]:
		box[1]-=1

	# Draving
	screen.fill((0,0,0))
	#pygame.draw.polygon(screen, (50,100,150),  (Vector2(-60,-60),Vector2(60,-60),Vector2(60,60),Vector2(0,80),Vector2(-60,60)))
	pygame.draw.rect(screen, (150,80,200),box, border_radius=15)
	pygame.display.flip()
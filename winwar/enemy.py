import pygame,sys
from pygame.math import Vector2
from pygame.locals import *

class Enemies(pygame.sprite.Sprite):
	"""docstring for Enemies"""
	def __init__(self, x, y): #, game):
		pygame.sprite.Sprite.__init__(self)
		self.picture = pygame.image.load('img/coronavirus.png')
		self.image = pygame.transform.scale(self.picture, (65,65))
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]
		self.counter = 0
		self.direction = 1

	def update(self):
		pass
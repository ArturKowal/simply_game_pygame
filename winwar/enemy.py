import pygame,sys
from pygame.math import Vector2
from pygame.locals import *
from random import randint as rand

class Enemies(pygame.sprite.Sprite):
	"""docstring for Enemies"""
	def __init__(self, x, y): #, game):
		pygame.sprite.Sprite.__init__(self)
		self.picture = pygame.image.load('img/coronavirus.png')
		self.image = pygame.transform.scale(self.picture, (65,65))
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]
		self.health = 2
		self.health_cur = self.health
		self.counter = 0
		self.direction = 1

	def update(self):
		# move to the right and next to the left
		self.rect.x += self.direction
		self.counter += 1
		if abs(self.counter) > 60:
			self.direction *= -1
			self.counter *= self.direction
		# mask
		self.mask = pygame.mask.from_surface(self.image)

class EnemiesAmmo(pygame.sprite.Sprite):
	"""docstring for EnemiesAmmo"""
	def __init__(self, x, y, game, player_group, player):
		pygame.sprite.Sprite.__init__(self)
		self.picture = pygame.image.load('img/corona_ammo' + str(rand(1,4)) + '.png')
		self.image = pygame.transform.scale(self.picture, (40,40))
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]
		self.size=game.screen.get_size()
		self.player_group = player_group
		self.player = player

	def update(self):
		self.rect.y += 3
		if self.rect.top >  self.size[1]:
			self.kill()

		if pygame.sprite.spritecollide(self, self.player_group, False, pygame.sprite.collide_mask):
			self.kill()
			#reduce spaceship health
			self.player.health_cur -= 1
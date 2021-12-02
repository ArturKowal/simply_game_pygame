import pygame,sys
from pygame.math import Vector2
from pygame.locals import *

class Ammo(pygame.sprite.Sprite):
	"""docstring for Ammo"""
	def __init__(self, x, y, enemy_group, enemyAmmo_group): #, game):
		pygame.sprite.Sprite.__init__(self)
		self.picture = pygame.image.load('img/syringe.png')
		self.image = pygame.transform.scale(self.picture, (50,50))
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]
		self.enemy_group = enemy_group
		self.enemyAmmo_group = enemyAmmo_group
		#self.size=game.screen.get_size()

	def update(self):
		self.rect.y -= 5
		if self.rect.bottom < 0:
			self.kill()
		if pygame.sprite.spritecollide(self, self.enemy_group, True, pygame.sprite.collide_mask):
			self.kill()
		if pygame.sprite.spritecollide(self, self.enemyAmmo_group, True):
			self.kill()
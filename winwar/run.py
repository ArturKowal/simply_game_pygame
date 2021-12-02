import pygame,sys
from pygame.locals import *
from player import Player
from ammo import Ammo
from enemy import Enemies, EnemiesAmmo
import random

class Game(object):
	""" class Game """
	def __init__(self):
		# Config
		self.fps=60
		self.rows = 3
		self.columns = 9
		self.enemy_bullet_cooldown = 800
		self.last_enemy_shot = pygame.time.get_ticks()

		# Init
		pygame.init()
		self.screen=pygame.display.set_mode((1000,550)) #1280/1.5,720/1.5
		picture = pygame.image.load("img/own_background.png")
		picture = pygame.transform.scale(picture, (1000,550))
		pygame.display.set_caption('Win War by Artur Kowal')
		self.clock=pygame.time.Clock()
		self.size=self.screen.get_size()

		self.player_group = pygame.sprite.Group()
		self.bullet_group = pygame.sprite.Group()
		self.enemy_group = pygame.sprite.Group()
		self.enemyAmmo_group = pygame.sprite.Group()
		
		self.player = Player(int(self.size[0]/2),self.size[1]-62,self,3, self.enemy_group,self.enemyAmmo_group)

		self.player_group.add(self.player)
		self.create_enemies()


		while True:
			# Drow background
			self.screen.blit(picture, (0, 0))
			# Ticking
			self.clock.tick(self.fps)

			# random alien bullet
			time_now = pygame.time.get_ticks()
			if time_now - self.last_enemy_shot > self.enemy_bullet_cooldown and len(self.enemyAmmo_group) < 4 and len(self.enemy_group) > 0:
				attack_enemy = random.choice(self.enemy_group.sprites())
				enemy_bullet = EnemiesAmmo(attack_enemy.rect.centerx,attack_enemy.rect.bottom,self,self.player_group, self.player)
				self.enemyAmmo_group.add(enemy_bullet)
				self.last_enemy_shot = time_now


			# Handle events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type ==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
					sys.exit(0)

			# Update
			self.player.update()
			self.bullet_group.update()
			self.enemy_group.update()
			self.enemyAmmo_group.update()


			# Draving
			self.player_group.draw(self.screen)
			self.bullet_group.draw(self.screen)
			self.enemy_group.draw(self.screen)
			self.enemyAmmo_group.draw(self.screen)

			pygame.display.update() #flip

	def create_enemies(self):
		for row in range(self.rows):
			for column in range(self.columns):
				enemy = Enemies(100 + column * 100, 75 + row * 100)
				self.enemy_group.add(enemy)


if __name__=="__main__":
	Game()



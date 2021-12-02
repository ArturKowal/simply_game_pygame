import pygame,sys
from pygame.locals import *
from player import Player
from ammo import Ammo
from enemy import Enemies

class Game(object):
	""" class Game """
	def __init__(self):
		# Config
		self.fps=60
		self.rows = 3
		self.columns = 9

		# Init
		pygame.init()
		self.screen=pygame.display.set_mode((1000,550)) #1280/1.5,720/1.5
		picture = pygame.image.load("img/own_background.png")
		picture = pygame.transform.scale(picture, (1000,550))
		pygame.display.set_caption('Win War by Artur Kowal')
		self.clock=pygame.time.Clock()
		self.size=self.screen.get_size()
		self.player = Player(int(self.size[0]/2),self.size[1]-62,self,3)

		self.player_group = pygame.sprite.Group()
		self.bullet_group = pygame.sprite.Group()
		self.enemy_group = pygame.sprite.Group()


		self.player_group.add(self.player)
		self.create_enemies()


		while True:
			# Handle events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type ==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
					sys.exit(0)

			self.screen.blit(picture, (0, 0))
			# Ticking
			self.clock.tick(self.fps)

			# Update
			self.player.update()
			self.bullet_group.update()
			self.enemy_group.update()


			# Draving
			self.player_group.draw(self.screen)
			self.bullet_group.draw(self.screen)
			self.enemy_group.draw(self.screen)

			pygame.display.update() #flip

	def create_enemies(self):
		for row in range(self.rows):
			for column in range(self.columns):
				enemy = Enemies(100 + column * 100, 75 + row * 100)
				self.enemy_group.add(enemy)

if __name__=="__main__":
	Game()



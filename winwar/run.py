import pygame,sys
from pygame import Vector2
from player import Player

class Game(object):
	""" class Game """
	def __init__(self):
		# Config
		self.max_tps=150.0

		# Init
		pygame.init()
		self.screen=pygame.display.set_mode((950,534)) #1280/1.5,720/1.5
		bg = pygame.image.load("background.png")
		self.tps_clock=pygame.time.Clock()
		self.tps_delta=0.0
		self.player = Player(self)

		while True:
			# Handle events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type ==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
					sys.exit(0)

			# Ticking
			self.tps_delta+=self.tps_clock.tick()/1000.0
			while self.tps_delta > 1 /self.max_tps:
				self.tick()
				self.tps_delta -=1/self.max_tps

			# Draving
			#self.screen.fill((0,0,0))
			self.screen.blit(bg, (0, 0))
			self.draw()
			pygame.display.flip()

					

	def tick(self):
		# Checking inputs
		#keys=pygame.key.get_pressed()
		self.player.tick()

	def draw(self):
		self.player.draw()

if __name__=="__main__":
	Game()
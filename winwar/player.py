import pygame,sys
from pygame.math import Vector2
from ammo import Ammo
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	"""docstring for Player"""
	def __init__(self, x, y, game, health, enemy_group, enemyAmmo_group):
		pygame.sprite.Sprite.__init__(self)
		self.picture = pygame.image.load('img/player.png')
		self.image = pygame.transform.scale(self.picture, (80,110))
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]
		self.size=game.screen.get_size()
		self.game = game
		self.health=health
		self.health_cur= health
		self.last_shot = pygame.time.get_ticks()
		self.enemy_group = enemy_group
		self.enemyAmmo_group = enemyAmmo_group

	def update(self):
		speed = 6
		cooldown = 500
		pressed=pygame.key.get_pressed()
		if (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]) and self.rect.left<self.size[0]-100:
			self.rect.x +=speed
		if (pressed[pygame.K_a] or pressed[pygame.K_LEFT]) and self.rect.right>100:
			self.rect.x -=speed

		time_now = pygame.time.get_ticks()
		if pressed[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
			bullet = Ammo(self.rect.centerx,self.rect.top, self.enemy_group, self.enemyAmmo_group)
			self.game.bullet_group.add(bullet)
			self.last_shot = time_now

		# mask
		self.mask = pygame.mask.from_surface(self.image)

		# draw health bar
		pygame.draw.rect(self.game.screen, (250,10,20), (self.rect.x, (self.rect.bottom + 2), self.rect.width, 10))
		if self.health_cur > 0:
			pygame.draw.rect(self.game.screen, (10,250,20), (self.rect.x, (self.rect.bottom + 2), int(self.rect.width * (self.health_cur / self.health)), 10))
		



		# self.game=game 
		# self.size=self.game.screen.get_size()
		# self.position=Vector2(self.size[0]/2,self.size[1]/2+200)
		# self.velocity=Vector2(0,0)
		# self.acceleration=Vector2(0,0)

	# def add_power(self,power):
	# 	self.acceleration += power

	# def tick(self):

	# 	pressed=pygame.key.get_pressed()
	# 	if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
	# 		self.add_power(Vector2(1,0))
	# 	if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
	# 		self.add_power(Vector2(-1,0))

	# 	# Physics
	# 	self.velocity *= 0.9
	# 	self.velocity += self.acceleration
	# 	self.position += self.velocity
	# 	self.acceleration *= 0
	# 	print('Player: ', self.position)
	# 	# Board limitation
	# 	if self.position.x>self.size[0]: self.position.x=self.size[0]-25
	# 	if self.position.x<0: self.position.x=25
	# 	if self.size[1]/2+200>self.position.y: self.position.y=self.size[1]/2+200

	# def draw(self):
	# 	#pygame.draw.rect(self.game.screen, (150,80,200),pygame.Rect(self.position.x,self.position.y,50,50), border_radius=15)
	# 	points=(Vector2(-5,5),Vector2(0,8),Vector2(5,5),Vector2(5,-5),Vector2(-5,-5))
	# 	points = [Vector2(p.x,p.y*-1) for p in points] # fix axis y
	# 	points= [self.position+p*2.5 for p in points]
	# 	pygame.draw.polygon(self.game.screen,(200,200,50), points)	



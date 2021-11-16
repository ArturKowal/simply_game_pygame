import pygame,sys
from pygame.math import Vector2

class Player(object):
	"""docstring for Player"""
	def __init__(self, game):
		self.game=game 
		size=self.game.screen.get_size()
		self.position=Vector2(size[0]/2,size[1]/2)
		self.velocity=Vector2(0,0)
		self.acceleration=Vector2(0,0)

	def add_power(self,power):
		self.acceleration += power

	def tick(self):

		pressed=pygame.key.get_pressed()
		if pressed[pygame.K_d]:
			self.add_power(Vector2(1,0))
		if pressed[pygame.K_s]:
			self.add_power(Vector2(0,1))
		if pressed[pygame.K_a]:
			self.add_power(Vector2(-1,0))
		if pressed[pygame.K_w]:
			self.add_power(Vector2(0,-1))

		# Physics
		self.velocity *= 0.8 
		self.velocity += self.acceleration
		self.position += self.velocity
		self.acceleration *= 0


	def draw(self):
		#pygame.draw.rect(self.game.screen, (150,80,200),pygame.Rect(self.position.x,self.position.y,50,50), border_radius=15)
		points=(Vector2(-5,5),Vector2(0,8),Vector2(5,5),Vector2(5,-5),Vector2(-5,-5))
		angle = self.velocity.angle_to(Vector2(0,1))
		points = [p.rotate(angle) for p in points]
		points = [Vector2(p.x*-1,p.y) for p in points]
		points= [self.position+p*3 for p in points]
		pygame.draw.polygon(self.game.screen,(200,200,50), points)	
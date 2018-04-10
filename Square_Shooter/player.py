import pygame
import random

WIDTH = 360
HEIGHT = 480

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
yellow = (255,255,0)
lblue =(0,255,255)

mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50,50))#creates a rectangle
		self.image.fill(purple)#fill shape with color
		self.rect = self.image.get_rect()#rectangle around image
		self.rect.center = (WIDTH/2, HEIGHT/2)#initial position
		self.speed = [0,0]
	def update(self):
		self.speed[0] = 0
		self.speed[1] = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed[0] = -3
		if keystate[pygame.K_d]:
			self.speed[0] = 3
		if keystate[pygame.K_w]:
			self.speed[1] = -3
		if keystate[pygame.K_s]:
			self.speed[1] = 3

		 
		self.rect.x+=self.speed[0]
		self.rect.y+=self.speed[1]	
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.x = 0
		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT
		if self.rect.top < 0:
			self.rect.y = 0

	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)

	def update_collision(self, status):
		self.rect.left = 0
		self.rect.top = 0

class Ground(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((WIDTH, 50))
		self.image.fill(green)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2,HEIGHT-20)
	def update(self):
		self.rect.x = self.rect.x
		self.rect.y = self.rect.y	

class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30,30))
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.rect.bottom = random.randrange(-8, -1)
		self.rect.x = random.randrange(50, WIDTH-50)
		self.speedx = random.randrange(1,3)
		self.speedy = random.randrange(2,8)
	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT:
			self.rect.bottom = random.randrange(-8,-1)
			self.speedy = random.randrange(2,8)
		if self.rect.left < 0:
			self.speedx = -self.speedx
		if self.rect.right > WIDTH:
			self.speedx = -self.speedx
 
class Bullet(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10,20))
		self.image.fill(yellow)
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

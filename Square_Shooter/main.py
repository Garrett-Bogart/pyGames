import sys, pygame
from player import * 
from score import *
from pygame.locals import *
import random
import time

def start_screen(FPS):
	waiting = True
	pygame.init()
	pygame.mixer.init()
	pygame.display.set_caption("My Game")
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	draw_text_center_top(screen, "SQUARE GAME!!!",40, WIDTH/2, HEIGHT/2)
	draw_text_center_top(screen, "press any key to continue",20, WIDTH/2, HEIGHT*3/4)
	while waiting:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYUP:
				waiting = False
		pygame.display.flip()

def clear():
	for sprite in all_sprites:
		sprite.kill()


def start():
	FPS = 30 
	score = 0
	hits = 0
	time1 = 0
	time2 = 0
	lives = 2

	running = True
	game_over = True
	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("My Game")
	clock = pygame.time.Clock()
	player = Player()
	all_sprites.add(player)
	for i in range(8):
		mob = Mob()
		all_sprites.add(mob)
		mobs.add(mob)


	while lives > 0:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player.shoot()

		all_sprites.update()

		bullet_hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
		if bullet_hits:
			score+=1
			mob = Mob()
			all_sprites.add(mob)
			mobs.add(mob)
		mob_hits = pygame.sprite.spritecollide(player,mobs,False)
		if mob_hits:
			time2 = time.time()#tick time of a hit
			if hits == 0:
				time1 = time.time()#tick time of first hit
				hits = hits + 1
				lives = lives -1 
				continue
			if time2 - time1 > 1: 
				time1 = time.time()
				hits= hits + 1
				lives = lives - 1
		screen.fill(black)
		all_sprites.draw(screen)
		draw_text_center_top(screen,"score: "+str(score), 18, WIDTH/2, 10)
		draw_text_center_top(screen, "lives: "+ str(lives),18, WIDTH/2, 30)
		pygame.display.flip()
	clear()

while(1):
	start_screen(30)
	start()


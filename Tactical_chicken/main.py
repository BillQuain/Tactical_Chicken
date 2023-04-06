# Tactical Chicken
# Bill Quain And Timothy Worthem

import pygame, sys
import button as bt
from settings import *
from pygame.math import Vector2 as vector
from player import Player
from pytmx.util_pygame import load_pygame
from sprite import Sprite, Bullet

class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.offset = vector()
		self.display_surface = pygame.display.get_surface()
		self.bg = pygame.image.load('LevelOneGround.png').convert()
		scale_factor = 4
		original_width, original_height = self.bg.get_size()

		# scale the map
		scaled_width = int(original_width * scale_factor)
		scaled_height = int(original_height * scale_factor)
		self.scaled_map = pygame.transform.scale(self.bg, (scaled_width,scaled_height))


	def customize_draw(self, player):
		self.offset.x = player.rect.centerx - WINDOW_WIDTH/2
		self.offset.y = player.rect.centery - WINDOW_HEIGHT/2
		self.display_surface.blit(self.scaled_map,-self.offset)

		for sprite in self.sprites():
			offset_rect = sprite.image.get_rect(center = sprite.rect.center)
			offset_rect.center -= self.offset
			self.display_surface.blit(sprite.image, offset_rect)



class Game:
	def __init__(self):

		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('TACTICAL CHICKEN by Bill And Tim')
		self.clock = pygame.time.Clock()
		self.bullet_surf = pygame.image.load("bullet.png").convert_alpha()

		# groups
		self.all_sprites = AllSprites()

		self.obstacles = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()



		self.setup()



		# TACTICAL CHICKEN title
		self.title_text = pygame.image.load('tactchicl.png').convert_alpha()
		self.title_rect = self.title_text.get_rect(center = (720,200))
		# chicken and uzi art
		self.menueArt_surf = pygame.image.load("./player/Right/0.png").convert_alpha()
		og_width, og_height = self.menueArt_surf.get_size()
		self.scale = 8
		self.scaled_chicken_art = pygame.transform.scale(self.menueArt_surf,(og_width * self.scale , og_height * self.scale))
		self.scaled_chicken_art_rect = self.scaled_chicken_art.get_rect(center = (350,540))

		# button images
		self.quit_butt_image = pygame.image.load("quit.png").convert_alpha()
		self.start_butt_image = pygame.image.load("StartBtn.png").convert_alpha()
		self.set_butt_image = pygame.image.load("settingsBtn.png").convert_alpha()
		# buttons

		self.start_button = bt.Button(self.start_butt_image, 600, 280, 4)
		self.settings_button = bt.Button(self.set_butt_image, 600, 380, 4)
		self.quit_button = bt.Button(self.quit_butt_image, 1150, 640, 1)

	def create_bullet(self, pos, direction):
		Bullet(pos, direction, self.bullet_surf, [self.bullets, self.all_sprites])

	def setup(self):
		tmx_map = load_pygame('LevelOne.tmx')
		for x, y, surf in tmx_map.get_layer_by_name('Buldings').tiles():
			Sprite((x*32,y*32),surf, [self.obstacles, self.all_sprites])

		for obj in tmx_map.get_layer_by_name('Entity Layer'):
			if obj.name == 'Player':
				self.player = Player(pos = (obj.x * 4, obj.y * 4),
									 groups = self.all_sprites,
									 path= "./player/",
									 collisions_sprites=self.obstacles,
									 create_bullets = self.create_bullet)

	def startgame(self,surface,dt):
		

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return

			# update groups
			self.all_sprites.update(dt)

			# draw groups
			self.display_surface.fill('black')
			# self.display_surface.blit(background,background_rect)
			# self.display_surface.blit(hud,hud_rect)
			self.all_sprites.customize_draw(self.player)
			pygame.display.update()

	def settings(self,surface):
		running = True
		while running:
			surface.fill((0, 0, 0))
			chicken = pygame.image.load("chicky2.png").convert_alpha()
			chicken_rect = chicken.get_rect(center=(740, 260))

			surface.blit(chicken, chicken_rect)
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return

			pygame.display.update()

	def run(self):
		while True:
			# event loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			# delta time so game runs at proper speed
			dt = self.clock.tick() / 1000
			# fills the background to green
			self.display_surface.fill((59,97,30))
			# display menue art and title
			self.display_surface.blit(self.scaled_chicken_art,self.scaled_chicken_art_rect)
			# self.display_surface.blit(self.menueArtGun_surf,self.menueArtGun_rect)
			self.display_surface.blit(self.title_text,self.title_rect)
			self.start_button.draw(self.display_surface)
			self.quit_button.draw(self.display_surface)
			self.settings_button.draw(self.display_surface)
			# button code
			if self.start_button.is_clicked():
				self.startgame(self.display_surface,dt)
			if self.settings_button.is_clicked():
				self.settings(self.display_surface)
			if self.quit_button.is_clicked():
				pygame.quit()
				sys.exit()

			pygame.display.update()


if __name__ == '__main__':
	game = Game()
	game.run()
#Tactical Chicken
#Bill Quain And Timothy Worthem

import pygame, sys
import button as bt
from settings import *
from pygame.math import Vector2 as vector
from player import Player

class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.offset = vector()
		self.display_surface = pygame.display.get_surface()
		self.bg = pygame.image.load('LevelOne.png').convert()
		scale_factor = 4
		original_width, original_height = self.bg.get_size()

		#scale the map
		scaled_width = int(original_width * scale_factor)
		scaled_height = int(original_height * scale_factor)
		self.scaled_map = pygame.transform.scale(self.bg, (scaled_width,scaled_height))


	def customize_draw(self,player):

		self.offset.x = player.rect.centerx - WINDOW_WIDTH/2
		self.offset.y = player.rect.centery - WINDOW_HEIGHT/2

		self.display_surface.blit(self.scaled_map,-self.offset)

		for sprite in self.sprites():
			offset_rect = sprite.image.get_rect(center = sprite.rect.center)
			offset_rect.center -= self.offset
			self.display_surface.blit(sprite.image,offset_rect)



class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('TACTICAL CHICKEN by Bill And Tim')
		self.clock = pygame.time.Clock()

		#groups
		self.all_sprites = AllSprites()
		self.setup()





		#TACTICAL CHICKEN title
		self.title_text = pygame.image.load('tactchicl.png').convert_alpha()
		self.title_rect = self.title_text.get_rect(center = (720,200))
		#chicken and uzi art
		self.menueArt_surf = pygame.image.load("chicky2.png").convert_alpha()
		self.menueArt_rect = self.menueArt_surf.get_rect(center = (350,540))
		self.menueArtGun_surf = pygame.image.load("uzi.png").convert_alpha()
		self.menueArtGun_rect = self.menueArtGun_surf.get_rect(center =(350,540))
		#button images
		self.quit_butt_image = pygame.image.load("quit.png").convert_alpha()
		self.start_butt_image = pygame.image.load("StartBtn.png").convert_alpha()
		self.set_butt_image = pygame.image.load("settingsBtn.png").convert_alpha()
		#buttons
		#(self,image_path,x,y, scale)
		self.start_button = bt.Button(self.start_butt_image,600,280,4)
		self.settings_button = bt.Button(self.set_butt_image, 600, 380, 4)
		self.quit_button = bt.Button(self.quit_butt_image, 1150, 640, 1)
		#self.start_button = bt.Button(600,280,self.start_butt_image,4)
		#self.settings_button = bt.Button(600,380,self.set_butt_image,4)
		#self.quit_button = bt.Button(1150,640,self.quit_but_image,1)

	def setup(self):
		self.player = Player((300,300),self.all_sprites,None,None)

	def startgame(self,surface,dt):
		surface.fill((160,153,100))
		background = pygame.image.load("levelOne.png").convert()
		background_rect = background.get_rect(center = (640,360))
		hud = pygame.image.load("gameHUD.png").convert_alpha()
		hud_rect = hud.get_rect(center=(880, 660))

		#surface.blit(background, background_rect)
		#surface.blit(hud, hud_rect)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return

			#update groups
			self.all_sprites.update(dt)

			#draw groups
			self.display_surface.fill('black')
			#self.display_surface.blit(background,background_rect)
			#self.display_surface.blit(hud,hud_rect)
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
			#delta time so game runs at proper speed
			dt = self.clock.tick() / 1000
			#fills the background to green
			self.display_surface.fill((59,97,30))
			#display menue art and title
			self.display_surface.blit(self.menueArt_surf,self.menueArt_rect)
			self.display_surface.blit(self.menueArtGun_surf,self.menueArtGun_rect)
			self.display_surface.blit(self.title_text,self.title_rect)
			self.start_button.draw(self.display_surface)
			self.quit_button.draw(self.display_surface)
			self.settings_button.draw(self.display_surface)
			#button code
			if self.start_button.is_clicked():
				self.startgame(self.display_surface,dt)
			if self.settings_button.is_clicked():
				self.settings(self.display_surface)
			if self.quit_button.is_clicked():
				pygame.quit()
				sys.exit()







			pygame.display.update()



'''def main():
	pygame.init()
	WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
	display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
	pygame.display.set_caption("Tactical Chicken by Bill and Tim")



	titleText = pygame.image.load("tactchicl.png").convert_alpha()
	titleText_rect = titleText.get_rect(center = (720,200))
	clk = pygame.time.Clock()

	menuArt_surf = pygame.image.load("chicky2.png").convert_alpha()
	menuArt_rect = menuArt_surf.get_rect(center = (320,540))

	menuArtGun_surf = pygame.image.load("uzi.png")
	menuArtGun_rect = menuArtGun_surf.get_rect(center = (350,540))

	quit_butt_image = pygame.image.load("quit.png").convert_alpha()
	start_butt_image = pygame.image.load("StartBtn.png").convert_alpha()
	sett_butt_image = pygame.image.load("settingsBtn.png").convert_alpha()

	quit_button = bt.Button(1150, 640, quit_butt_image, 1)
	start_button = bt.Button(600,280,start_butt_image,4)
	settings_button = bt.Button(600,380,sett_butt_image,4)


	gameState = True
	while gameState:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		clk.tick(60)

		display_surface.fill((59,97,30))

		display_surface.blit(menuArt_surf,menuArt_rect)
		display_surface.blit(menuArtGun_surf,menuArtGun_rect)
		display_surface.blit(titleText,titleText_rect)

		if quit_button.draw(display_surface) == True:
			gameState = False

		if start_button.draw((display_surface)) ==True:
			startgame(display_surface)

		if settings_button.draw((display_surface)) == True:
			settings(display_surface)


		pygame.display.update()

	return

def startgame(surface):
	running = True
	while running:
		surface.fill((160,153,100))
		background  = pygame.image.load("background.png").convert_alpha()
		background_rect = background.get_rect(center = (640,360))
		hud = pygame.image.load("gameHUD.png").convert_alpha()
		hud_rect = hud.get_rect(center = (880,660))


		surface.blit(background,background_rect)
		surface.blit(hud,hud_rect)

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return

		pygame.display.update()


def settings(surface):
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
'''
if __name__ == '__main__':
	game = Game()
	game.run()
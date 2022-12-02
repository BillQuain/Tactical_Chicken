#Tactical Chicken
#Bill Quain And Timothy Worthem

import pygame, sys
import button as bt


def main():
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

if __name__ == '__main__':
    main()
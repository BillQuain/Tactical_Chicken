#Tactical Chicken
#Bill Quain And Timothy Worthem

import pygame, sys
import button as bt


def main():
    pygame.init()
    WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
    display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Tactical Chicken by Bill and Tim")


    font = pygame.font.Font('/Windows/Fonts/Arial.ttf', 100)
    titleText = font.render("TACTICAL CHICKEN", True, (255,255,255))
    titleText_rect = titleText.get_rect(center = (640,180))
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

        start_button.draw(display_surface)
        settings_button.draw(display_surface)

        if quit_button.draw(display_surface) == True:
            gameState = False

        pygame.display.update()

    return



if __name__ == '__main__':
    main()
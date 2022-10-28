#Tactical Chicken
#Bill Quain And Timothy Worthem

import pygame, sys



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

    startButt_surf = pygame.Surface((200,50))
    startButt_rect = startButt_surf.get_rect(center = (640,280))

    settButt_surf = pygame.Surface((200, 50))
    settButt_rect = settButt_surf.get_rect(center=(640, 380))

    quitButt_surf = pygame.Surface((200,50))
    quitButt_rect = quitButt_surf.get_rect(bottomright = (1280,720))

    gameState = True
    while gameState:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clk.tick(60)

        display_surface.fill((59,97,30))
        quitButt_surf.fill((138, 41, 34))
        startButt_surf.fill((135,115,72))
        settButt_surf.fill((135,115,72))
        display_surface.blit(menuArt_surf,menuArt_rect)
        display_surface.blit(menuArtGun_surf,menuArtGun_rect)
        display_surface.blit(titleText,titleText_rect)
        display_surface.blit(startButt_surf,startButt_rect)
        display_surface.blit(settButt_surf,settButt_rect)
        display_surface.blit(quitButt_surf,quitButt_rect)
        pygame.display.update()

    return



if __name__ == '__main__':
    main()
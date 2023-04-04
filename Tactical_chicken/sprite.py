import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = self.scale(surf)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-self.rect.height /3)

    #scaler method
    def scale(self, surf):
        scale_factor = 4
        original_width, original_height =  surf.get_size()

        # scale the sprites
        scaled_width = int(original_width * scale_factor)
        scaled_height = int(original_height * scale_factor)

        return pygame.transform.scale(surf, (scaled_width,scaled_height))


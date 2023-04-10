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


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, surf, groups, source):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(center = pos)
        self.source = source

        #float based movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = direction
        self.speed = 900

    def update(self,dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))





    #bullet scale method
    def scale(self, surf):
        scale_factor = 4
        original_width, original_height =  surf.get_size()

        # scale the sprites
        scaled_width = int(original_width * scale_factor)
        scaled_height = int(original_height * scale_factor)

        return pygame.transform.scale(surf, (scaled_width,scaled_height))

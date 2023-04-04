import pygame


# button class
class Button():
    def __init__(self, image_path, x, y, scale):
        width = image_path.get_width()
        height = image_path.get_height()
        self.image = pygame.transform.scale(image_path, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return pygame.mouse.get_pressed()[0]
        return False

import pygame
from pygame.math import Vector2 as vector


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, path, collisions_sprites):
        super().__init__(groups)
        self.status = 'Down'


        self.image = pygame.image.load("./player/Down/0.png")
        self.rightimage = pygame.image.load('./player/Right/0.png')
        self.leftimage = pygame.image.load('./player/Left/0.png')
        self.upimage = pygame.image.load('./player/Up/0.png')
        self.downimage= pygame.image.load('./player/Down/0.png')
        self.rect = self.image.get_rect(center = pos)

        #float based movement
        self.pos = vector(self.rect.center)
        self.direction = vector()
        self.speed = 200

        #collisions
        self.hitbox = self.rect.inflate(0,-self.rect.height/2)
        self.collision_sprites = collisions_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.image = self.rightimage
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.image = self.leftimage
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.image = self.upimage
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.image = self.downimage
        else:
            self.direction.y = 0

    def move(self, dt):
        # normalize vector
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x *self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        # horizontal collision


        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')

    def collision(self,direction):
        for sprite in self.collision_sprites.sprites():
            if sprite.hitbox.colliderect(self.hitbox):
                if direction == 'horizontal':
                    if self.direction.x > 0: #moving to the right
                        self.hitbox.right = sprite.hitbox.left
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                else: # vertical
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery

    def update(self, dt):
        self.input()
        self.move(dt)




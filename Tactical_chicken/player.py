import pygame
from pygame.math import Vector2 as vector
from os import walk

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,path, collisions_sprites):
        super().__init__(groups)
        self.import_assets(path)
        self.image = pygame.image.load("./player/RwhiteChickScaled.png")



        self.rect = self.image.get_rect(center = pos)

        #float based movement
        self.pos = vector(self.rect.center)
        self.direction = vector()
        self.speed = 100

        #collisions
        self.hitbox = self.rect.inflate(0,-self.rect.height/2)
        self.collision_sprites = collisions_sprites

    def import_assets(self,path):
        self.animations = {}

        for index,folder in enumerate(walk(path)):
            if index == 0:
                for name in folder[2]:
                    self.animations[name] = []
        print(self.animations)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self,dt):
        #normalize vector
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        #horizontal movement
        self.pos.x += self.direction.x *self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx

        #horizontal collision

        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery

    def update(self,dt):
        self.input()
        self.move(dt)




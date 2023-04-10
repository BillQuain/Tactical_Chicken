import pygame, sys
from pygame.math import Vector2 as vector


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups,path, collisions_sprites, create_bullets):
        super().__init__(groups)
        self.status = 'Down'
        self.health = 100
        self.is_vulnerable = True
        self.hit_time = None

        self.image = pygame.image.load("./player/Down/0.png")
        self.rightimage = pygame.image.load('./player/Right/0.png')
        self.leftimage = pygame.image.load('./player/Left/0.png')
        self.upimage = pygame.image.load('./player/Up/0.png')
        self.downimage= pygame.image.load('./player/Down/0.png')
        self.rect = self.image.get_rect(center = pos)

        #float based movement
        self.pos = vector(self.rect.center)
        self.direction = vector()
        self.speed = 250

        #collisions
        self.hitbox = self.rect.inflate(0,-self.rect.height/2)
        self.collision_sprites = collisions_sprites

        #attack
        self.attacking  = False
        self.create_bullet = create_bullets
        self.shootTime = None

    def damage(self):
        if self.is_vulnerable:
            self.health -= 10
            self.is_vulnerable = False
            self.hit_time = pygame.time.get_ticks()
            if self.health <= 0:
                print("dead")

    def check_death(self):
        if self.health <= 0:
            pygame.quit()
            sys.exit()

    def vulnerability_timer(self):
        if not self.is_vulnerable:
            current_time = pygame.time.get_ticks()
            if current_time - self.hit_time > 400:
                self.is_vulnerable = True

    def input(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.image = self.rightimage
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.image = self.leftimage
            self.status = "left"
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.image = self.upimage
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.image = self.downimage
            self.status = "down"
        else:
            self.direction.y = 0


        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.direction = vector()
            self.shootTime = pygame.time.get_ticks()
            if self.status == "right":
                self.create_bullet((self.rect.x+ 50, self.rect.y) , vector(1,0), "player")
            elif self.status == "left":
                self.create_bullet((self.rect.x -50, self.rect.y) , vector(-1,0), "player")
            elif self.status == "up":
                self.create_bullet((self.rect.x, self.rect.y -50)  , vector(0,-1), "player")
            elif self.status == "down":
                self.create_bullet((self.rect.x, self.rect.y +50) , vector(0,1), "player")

        self.bulletTimer(150)



    def bulletTimer(self, duration = 100):
        if self.attacking:
            current_time = pygame.time.get_ticks()
            if current_time - self.shootTime >= duration:
                self.attacking = False



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
        self.check_death()
        self.input()
        self.move(dt)
        self.vulnerability_timer()




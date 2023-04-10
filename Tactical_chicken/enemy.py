import pygame
from pygame.math import Vector2 as vector

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collisions_sprites, create_bullets, player):
        super().__init__(groups)
        #player assets
        self.image = pygame.image.load("./enemy/Down/0.png")
        self.rightimage = pygame.image.load('./enemy/Right/0.png')
        self.leftimage = pygame.image.load('./enemy/Left/0.png')
        self.upimage = pygame.image.load('./enemy/Up/0.png')
        self.downimage = pygame.image.load('./enemy/Down/0.png')
        self.turkeyplate = pygame.image.load('./enemy/Dead/0.png')
        self.rect = self.image.get_rect(center=pos)
        # enemy code made from player code
        self.player = player
        self.vision_radius = 550
        self.walk_radius = 450
        self.attack_radius = 200
        self.status = 'down'
        self.health = 100
        self.shootTime = None
        self.is_vulnerable = True
        # float based movement
        self.pos = vector(self.rect.center)
        self.direction = vector()
        self.speed = 100

        #bullets
        self.create_bullet = create_bullets
        self.bullet_shot = False

        # collisions
        self.hitbox = self.rect.inflate(0, -self.rect.height / 2)
        self.collision_sprites = collisions_sprites

        # attack
        self.attacking = False
        self.create_bullet = create_bullets
        self.shootTime = None

    def attack(self):
        distance = self.get_player_distance_direction()[0]
        if distance < self.attack_radius and not self.attacking:
            self.attacking = True
            self.bullet_shot = True
            self.shootTime = pygame.time.get_ticks()
            if self.status == "right":
                self.create_bullet((self.rect.x+ 50, self.rect.y), vector(1,0), "turkey")
            elif self.status == "left":
                self.create_bullet((self.rect.x -50, self.rect.y), vector(-1,0), "turkey")
            elif self.status == "up":
                self.create_bullet((self.rect.x, self.rect.y -50), vector(0,-1), "turkey")
            elif self.status == "down":
                self.create_bullet((self.rect.x, self.rect.y +50), vector(0,1), "turkey")
        self.bulletTimer(750)

    def bulletTimer(self, duration=100):
        if self.attacking:
            current_time = pygame.time.get_ticks()
            if current_time - self.shootTime >= duration:
                self.attacking = False

    def damage(self):
        if self.is_vulnerable:
            self.health -= 25
            self.is_vulnerable = False
            self.hit_time = pygame.time.get_ticks()


    def check_death(self):
        if self.health <= 0:
            self.image = self.turkeyplate
            self.speed = 0
            self.attacking = False
            self.attack_radius = 0
            self.vision_radius = 0
            self.walk_radius = 0
            self.is_vulnerable = False


    def vulnerability_timer(self):
        if not self.is_vulnerable:
            current_time = pygame.time.get_ticks()
            if current_time - self.hit_time > 100:
                self.is_vulnerable = True

    def get_player_distance_direction(self):
        enemy_pos = vector(self.rect.center)
        player_pos = vector(self.player.rect.center)
        distance = (player_pos - enemy_pos).magnitude()
        if distance != 0:
            direction=(player_pos- enemy_pos).normalize()
        else:
            direction = vector()
        return (distance,direction)

    def walk_to_player(self):
        distance, direction = self.get_player_distance_direction()
        if self.attack_radius < distance < self.walk_radius:
            self.direction = direction
        else:
            self.direction = vector()

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

    def face_player(self):
        distance, direction = self.get_player_distance_direction()

        if distance < self.vision_radius:
            if -0.5 < direction.y < 0.5:
                if direction.x < 0:
                    self.status = 'left'
                    self.image = self.leftimage
                elif direction.x > 0:
                    self.status = 'right'
                    self.image = self.rightimage
            else:
                if direction.y < 0:
                    self.status = 'up'
                    self.image = self.upimage
                elif direction.y > 0:
                    self.status = 'down'
                    self.image = self.downimage

    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if sprite.hitbox.colliderect(self.hitbox):
                if direction == 'horizontal':
                    if self.direction.x > 0:  # moving to the right
                        self.hitbox.right = sprite.hitbox.left
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                else:  # vertical
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery

    def update(self, dt):
        self.face_player()
        self.walk_to_player()
        self.check_death()
        self.attack()
        self.move(dt)
        self.vulnerability_timer()


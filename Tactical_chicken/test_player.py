import unittest

import pygame.time
from pygame.math import Vector2 as vector
from player import Player
from unittest.mock import MagicMock

class TestPlayer(unittest.TestCase):


    def setUp(self):
        pygame.init()
        self.collision_sprites = pygame.sprite.Group()
        self.group = pygame.sprite.Group()
        self.player = Player((1,1), self.group, None, self.collision_sprites, None)

    def test_damage(self):
        self.player.health = 100
        self.player.is_vulnerable = True
        self.player.damage()

        self.assertEqual(self.player.health, 90)
        self.assertFalse(self.player.is_vulnerable)

    def test_vulnerability_timer(self):
        self.player.is_vulnerable = False
        self.player.hit_time = 0
        pygame.time.get_ticks = MagicMock(return_value = 0)

        self.player.vulnerability_timer()
        self.assertFalse(self.player.is_vulnerable)

        pygame.time.get_ticks = MagicMock(return_value = 500)
        self.player.vulnerability_timer()
        self.assertTrue(self.player.is_vulnerable)


    def test_input(self):
        # create a fake event to simulate key presses
        right_key_down = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_RIGHT)
        left_key_down = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
        up_key_down = pygame.event.Event(pygame.KEYDOWN, key =pygame.K_UP)
        down_key_down = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_DOWN)
        space_key_down = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_SPACE)

        # test right arrow
        pygame.event.post(right_key_down)
        self.assertTrue(right_key_down)

        # test left arrow
        pygame.event.post(left_key_down)
        self.assertTrue(left_key_down)

        # test up key
        pygame.event.post(up_key_down)
        self.assertTrue(up_key_down)

        # test down key
        pygame.event.post(down_key_down)
        self.assertTrue(down_key_down)

        pygame.event.post(space_key_down)
        self.assertTrue(space_key_down)








    def test_bullet_timer(self):
        pygame.time.get_ticks = MagicMock(return_value = 0)
        self.player.shootTime = 0
        self.player.attacking = True

        self.player.bulletTimer(100)
        self.assertTrue(self.player.attacking)

        pygame.time.get_ticks = MagicMock(return_value = 101)
        self.player.bulletTimer(100)
        self.assertFalse(self.player.attacking)
    def test_move(self):
        self.player.direction = vector(1,0)
        self.player.speed = 10
        self.player.pos = vector(0,0)

        self.player.move(1)

        self.assertEqual(self.player.pos, vector(10,0))




if __name__ == '__main__':
    unittest.main()

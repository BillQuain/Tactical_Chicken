import unittest
import pygame.sprite
from pygame.math import Vector2 as vector
from enemy import Enemy
from player import Player
from unittest.mock import MagicMock

class TestEnemy(unittest.TestCase):


    def setUp(self):
        self.group = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.player = Player((100, 0), self.group, None, self.collision_sprites, None)
        self.enemy = Enemy((200, 0), self.enemyGroup, self.collision_sprites, None, self.player)

    def test_attack(self):
        distance, direction = self.enemy.get_player_distance_direction()

        # Checks if enemy is within range
        self.assertLess(distance, self.enemy.vision_radius)
        # checks if enemy is currently attacking
        self.assertEqual(self.enemy.attacking, False)




    def test_bulletTimer(self):
        pygame.time.get_ticks = MagicMock(return_value=0)
        self.enemy.shootTime = 0
        self.enemy.attacking = True

        self.enemy.bulletTimer(100)
        self.assertTrue(self.enemy.attacking)

        pygame.time.get_ticks = MagicMock(return_value=101)
        self.enemy.bulletTimer(100)
        self.assertFalse(self.enemy.attacking)
        
    def test_damage(self):
        self.enemy.health = 100
        self.enemy.is_vulnerable = True
        self.enemy.damage()

        self.assertEqual(self.enemy.health, 75)
        self.assertFalse(self.enemy.is_vulnerable)
        
    def test_check_death(self):
        self.enemy.health = 0
        self.assertEqual(self.enemy.health, 0)
        
    def test_vulnerability_timer(self):
        self.enemy.is_vulnerable = False
        self.enemy.hit_time = 0
        pygame.time.get_ticks = MagicMock(return_value=0)

        self.enemy.vulnerability_timer()
        self.assertFalse(self.enemy.is_vulnerable)

        pygame.time.get_ticks = MagicMock(return_value=500)
        self.enemy.vulnerability_timer()
        self.assertTrue(self.enemy.is_vulnerable)

    def test_get_player_distance_direction(self):
        distance, direction = self.enemy.get_player_distance_direction()

        # This will check if the distance is equal to 100
        self.assertEqual(distance, 100)

        expected_direction = (-1, 0)
        # This will check what direction the player is from the enemy
        self.assertEqual(direction.x, expected_direction[0])
        self.assertEqual(direction.y, expected_direction[1])

    def test_move(self):
        self.enemy.direction = vector(1, 0)
        self.enemy.speed = 10
        self.enemy.pos = vector(0, 0)

        self.enemy.move(1)

        self.assertEqual(self.enemy.pos, vector(10, 0))

    def test_face_player(self):
        checkFace = 'left'
        distance, direction = self.enemy.get_player_distance_direction()

        self.enemy.face_player()

        # this will check if distance is less than vision
        self.assertLess(distance, self.enemy.vision_radius)
        # this will check if the enemy is facing the correct direction
        self.assertEqual(checkFace, self.enemy.status)


if __name__ == '__main__':
    unittest.main()

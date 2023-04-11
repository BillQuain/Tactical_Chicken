import unittest
from enemy import Enemy


class TestEnemy(unittest.TestCase):


    def setUp(self):
        self.enemy = Enemy((1,1), None, None, None, None)

    def test_attack(self):
        pass

    def test_bulletTimer(self):
        pass
        
    def test_damage(self):
        pass
        
    def test_check_death(self):
        pass
        
    def test_vulnerability_timer(self):
        pass

    def test_get_player_distance_direction(self):
        pass

    def test_walk_to_player(self):
        pass

    def test_move(self):
        pass

    def test_face_player(self):
        pass

    def test_collision(self):
        pass



if __name__ == '__main__':
    unittest.main()

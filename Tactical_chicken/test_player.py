import unittest
from player import Player

class TestPlayer(unittest.TestCase):


    def setUp(self):
        self.player = Player((1,1), None, None, None, None)
    def test_damage(self):
        self.assertEqual(True, False)  # add assertion here

    def test_vulnerability_timer(self):
        self.assertEqual(True,False)

    def test_input(self):
        self.assertEqual(True,False)

    def test_bullet_timer(self):
        self.assertEqual(True,False)

    def test_move(self):
        self.assertEqual(True,False)

    def test_collisions(self):
        self.assertEqual(True,False)



if __name__ == '__main__':
    unittest.main()

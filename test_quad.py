import unittest
from quad import quad

class TestQuad(unittest.TestCase):
    def test_quad(self):
        self.assertEqual(quad(3), 12)
        self.assertEqual(quad(0), 0)
        self.assertEqual(quad(-1), -4)

if __name__ == '__main__':
    unittest.main()
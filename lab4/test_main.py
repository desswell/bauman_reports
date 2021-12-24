import unittest
from unittest.mock import patch, Mock
from main import disc
import math

class TestRoots(unittest.TestCase):

    def test_roots_is_equal(self):
        self.assertEqual(disc(1, -5, 6), 1.0)
        self.assertEqual(disc(1, -4, 4), 0.0)
        self.assertEqual(disc(-4, 16, 0), 16.0)
        self.assertEqual(disc(1, 0, -16), 8.0)

    def test_string_root(self):
        self.assertRaises(TypeError, disc, 'abobas')
        self.assertRaises(TypeError, disc, False)
        self.assertRaises(TypeError, disc, [3, 1])

if __name__ == '__main__':
    unittest.main()
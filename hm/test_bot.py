import unittest
from translate import raschet
class TestRoots(unittest.TestCase):

    def test_roots_is_equal(self):
        self.assertEqual(raschet(73.35, 83.16, 100), 88.2034632034632)

    def test_string_root(self):
        self.assertRaises(TypeError, raschet, "pepa")

if __name__ == '__main__':
    unittest.main()
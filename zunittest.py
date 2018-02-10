import z
import unittest

class TestStats(unittest.TestCase):
    def test_average(self):
        self.assertEqual(z.average([20, 30, 70]), 40.0)
    def test_count(self):
        self.assertEqual(z.count('banana', 'a'), 3)
        self.assertEqual(z.count('banana', 'b'), 1)
        self.assertEqual(z.count('banana', 'n'), 2)
    def test_find(self):
        self.assertEqual(z.find('banana', 'a'), 1)
        self.assertEqual(z.find('banana', 'a', 2), 3)
        self.assertEqual(z.find('banana', 'a', 1), 1)
        self.assertEqual(z.find('banana', 'b'), 0)

unittest.main()

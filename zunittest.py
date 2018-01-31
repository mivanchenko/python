import z
import unittest

class TestStats(unittest.TestCase):
    def test_average(self):
        self.assertEqual(z.average([20, 30, 70]), 40.0)

unittest.main()

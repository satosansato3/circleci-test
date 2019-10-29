import unittest
from sum import sum_test


class TestSum(unittest.TestCase):
    def test_sum(self):
        assert sum_test(1, 2) == 3

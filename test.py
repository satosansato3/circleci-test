import unittest
import sum


class SumTest(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_sum(self):
        self.assertEqual(3, sum.sum_test(1, 2))

if __name__ == "__main__":
    unittest.main()
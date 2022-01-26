import unittest
from money_change_again import change, change_naive


class MoneyChangeAgain(unittest.TestCase):
    def test_money(self):
        self.assertEqual(change(2), 2)
        self.assertEqual(change(4), 1)
        self.assertEqual(change(6), 2)

    def test_small(self):
        for money in range(1, 40):
            self.assertEqual(change(money), change_naive(money))

    def test_large(self):
        for money, answer in ((200, 50), (239, 60), (34, 9)):
            self.assertEqual(change(money), answer)


if __name__ == '__main__':
    unittest.main()

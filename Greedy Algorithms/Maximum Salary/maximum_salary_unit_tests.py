import copy
import unittest
from random import randint
from maximum_salary import largest_number_naive, largest_number, num_is_larger_than_max


class TestLargestNumber(unittest.TestCase):
    def test_is_larger(self):
        self.assertFalse(num_is_larger_than_max("284", "28"))  # max_num, num
        self.assertFalse(num_is_larger_than_max("3", "19"))
        self.assertFalse(num_is_larger_than_max("2845", "284"))
        self.assertFalse(num_is_larger_than_max("2123", "212"))
        self.assertFalse(num_is_larger_than_max("2112", "211"))
        self.assertTrue(num_is_larger_than_max("2111", "211"))
        self.assertTrue(num_is_larger_than_max("21", "2"))

    def test_small(self):
        for numbers in [
            (['44', '41', '4'], 44441),
            (['2', '21', '23', '211', '213', '231', '232'], 23232231221321211),
            (['28', '321', '610', '187', '778', '740', '807', '284'], 80777874061032128428187),
            (['1000'], 1000),
            (['21', '211'], 21211),
            (['19', '3'], 319),
            (['3', '19'], 319),
            (['1', '12'], 121),
            (['1'], 1),
            (['1', '2'], 21),
            (['21', '2'], 221),
            (['9', '4', '6', '1', '9'], 99641),
            (['23', '39', '92'], 923923),
            (['1', '12'], 121),
            (['2', '12'], 212),
            (['2', '21'], 221),
            (['2', '21', '23', '211', '213', '231', '232'], 23232231221321211)
        ]:
            print(numbers[0])
            self.assertEqual(largest_number(numbers[0]), numbers[1])
            # self.assertEqual(largest_number(numbers),largest_number_naive(numbers))

    def test_random(self):
        for n in range(2, 15):
            for max_value in [10, 20, 100, 1000]:
                for _ in range(10):
                    numbers = [randint(1, max_value) for _ in range(n)]
                    input_num = list(map(str, numbers))
                    numbers_copy = copy.deepcopy(input_num)
                    print(numbers)
                    self.assertEqual(largest_number(input_num),
                                     largest_number_naive(numbers_copy))

    def test_1(self):
        numbers = ['1'] * 100
        self.assertEqual(int(''.join(numbers)), largest_number(numbers))

    def test_2(self):
        numbers = ['1000'] * 100
        self.assertEqual(int(''.join(numbers)), largest_number(numbers))


if __name__ == '__main__':
    unittest.main()

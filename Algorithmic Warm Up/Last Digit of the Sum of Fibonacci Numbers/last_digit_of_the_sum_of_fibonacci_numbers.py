# python3
"""
File name: last_digit_of_the_sum_of_fibonacci_numbers.py
Author: Sayuri Monarrez Yesaki
Date created: 1/13/2022
Date last modified: 1/13/2022
Python version: 3.8

The goal of this problem is to find the last digit of a sum of the first n Fibonacci numbers.

Task: Given an integer n, find the last digit of the sum F0 + F1 + ... + Fn.

Input: Single integer n.

Constraint: 0 <= n <= 10^18

Output: Last digit of F0 + F1 + ... + Fn.
"""

"""
This naive algorithm was provided by the instructors.

:param: n <int> - Fn
"""


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n: int) -> int:
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


"""
The Pisano Period is the period with which the sequence of Fibonacci numbers taken
modulo n repeats. (https://en.wikipedia.org/wiki/Pisano_period)
 
Since the goal is to calculate the last digit of the sum of fibonacci numbers, the only
number needed of each Fibonacci number is their last digit. In other words, Fibonacci number modulo 10.
The Pisano Period or sequence of Fibonacci number modulo 10 is already known:
    
    PISANO_PERIOD_10 = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9,
                        9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]

    and has a length of 60.

Algorithm:
1. If n <= 60, sum the first n + 1 elements of the known pisano period of ten. 
2. If n > 60, calculate the remainder and quotients of n and 60. Then, add the product of the quotient with the 
    sum of all elements in the pisano period of 10 with the sum of 0,...,remainder+1 elements in the pisano period.
3. Get the last digit of the sum using modulus 10.
"""


def last_digit_of_the_sum_of_fibonacci_numbers(n: int) -> int:
    assert 0 <= n <= 10 ** 18

    # The Pisano period of 10 of length 60.
    # The Pisano Period of 10 was obtained from here: https://en.wikipedia.org/wiki/Pisano_period
    PISANO_PERIOD_10_LEN = 60
    PISANO_PERIOD_10 = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9,
                        9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]

    if n <= PISANO_PERIOD_10_LEN:
        calc_sum = sum(PISANO_PERIOD_10[: n + 1])
        return calc_sum % 10
    else:
        remainder = n % PISANO_PERIOD_10_LEN
        quotient = n // PISANO_PERIOD_10_LEN

        calc_sum = sum(PISANO_PERIOD_10) * quotient + sum(PISANO_PERIOD_10[:remainder + 1])

        return calc_sum % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))

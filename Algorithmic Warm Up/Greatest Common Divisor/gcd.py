# python3
"""
File name: gcd.py
Author: Sayuri Monarrez Yesaki
Date created: 11/10/2021
Date last modified: 11/10/2021
Python version: 3.8

For integers a and b, their greatest common divisor or gdc(a,b) is the largest integer d so that d
divides both a and b.

Task: Given two integers a and b, find their greatest common divisor using the Euclidean algorithm.

Input: The two integers a, b are given in the same line separated by space.

Constraints: 1 <= a, b <= 2X 10 ^ 9

Output: integer.
"""

"""
This naive algorithm was provided by the instructors.

Very slow, it runs through the for loop many times. 
Runtime approx. a+b.

:param: a <int> - 
:param: b <int> - 
"""


def gcd_naive(a: int, b: int) -> int:
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    # biggest number seen so far.
    current_gcd = 1
    # check all numbers that are valid.
    for d in range(2, min(a, b) + 1):
        # the number divides both a and b.
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


"""
Let a' be the remainder when a is divided by b, then
    gcd(a, b) = gcd(a', b) = gcd(b, a')

a = a' + bq for some q
d divides a and b if and only if it divides a' and b

Runtime:
Each step reduces the size of numbers by about a factor of 2
log(ab) steps

:param: a <int> - 
:param: b <int> -
"""


def gcd(a: int, b: int) -> int:
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    # Base case - everything divides zero. Return a in this case.
    if b == 0:
        return a
    a_ = a % b
    return gcd(b, a_)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))

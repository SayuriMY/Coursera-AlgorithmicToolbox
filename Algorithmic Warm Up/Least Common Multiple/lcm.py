# python3
"""
File name: lcm.py
Author: Sayuri Monarrez Yesaki
Date created: 11/10/2021
Date last modified: 11/10/2021
Python version: 3.8

The least common multiple of two positive integers a and b is the least positive integer m that is divisible by both
a and b.

Task: Given two integers a and b, find their least common multiple.

Input: Two int a and b are given in the same line separated by space.

Constraints: 1 <= a, b <= 2X 10 ^ 9

Output: integer - the least common multiple of a and b.
"""

"""
This naive algorithm was provided by the instructors.

:param: a <int> - 
:param: b <int> - 
"""


def lcm_naive(a: int, b: int) -> int:
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


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


def euclidean_gdc(a: int, b: int) -> int:
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    # Base case - everything divides zero. Return a in this case.
    if b == 0:
        return a
    a_ = a % b
    return euclidean_gdc(b, a_)


"""
The least common multiple of a and b is their product divided by their greatest common divisor (GCD).
lcm(a, b) = ab/gcd(a,b)

:param: a <int> - 
:param: b <int> -
"""


def lcm(a: int, b: int) -> int:
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    # Find GCD using euclidean algorithm.
    gcd = euclidean_gdc(a, b)

    return (a * b) // gcd


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))

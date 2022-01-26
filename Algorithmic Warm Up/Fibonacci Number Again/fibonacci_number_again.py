# python3
"""
File name: fibonacci_number_again.py
Author: Sayuri Monarrez Yesaki
Date created: 10/25/2021
Date last modified: 11/8/2021
Python version: 3.8

The goal of this problem is to compute Fn modulo m, where n may be up to 10^18. For such values, an
algorithm looping for n iterations will not fit into one second for sure.

Hint: To solve this problem without going through all Fi for i from 0 to n let's see what happens when
m is small

    i       0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15      period
---------------------------------------------------------------------------------------
    Fi      0   1   1   2   3   5   8   13  21  34  55  89  144 233 377 610
Fi mod 2    0   1   1   0   1   1   0   1   1   0   1   1   0   1   1   0        011
Fi mod 3    0   1   1   2   0   2   2   1   0   1   1   2   0   2   2   1       01120221
Fi mod 10   0   1   1   2   3   5   8   3   1   4   5   9   4   3   7   0

Example: F2015 mod 3
 - Find the remainder of 2015 when divided by 8.
 2015 = 251 * 8 + 7
 F 2015 mod 3 = F7 mod 3 = 1

This is true in general: for any integer m >= 2, the sequence Fn mod m is periodic. The period
always starts with 01 and is known as Pisano period.

Task: Given two integers n and m, output Fn modulo m ( that is the remainder of Fn when divided by m).

Input: Two integers: n and m given on the same line (separated by space).

Constraints: 1 <= n <= 10^18, 2 <= m <= 10^3

Output: Output Fn mod m.
"""


"""
This naive algorithm was provided by the instructors.

:param: n <int> - Fn
:param: m <int> - 
"""


def fibonacci_number_again_naive(n: int, m: int) -> int:
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


"""
This algorithm was obtained from 
https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/

It calculates and returns the length of the Pisano Period for a given number m.
"""


def get_pisano_period_length(m: int) -> int:
    previous = 0
    current = 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # Pisano periods start with 01.
        # If previous is 0 and current is 1, it means
        # the period is starting again.
        if (previous == 0) and (current == 1):
            return i + 1


"""
This algorithm calculates Fn mod m by:
    1. Find the length of the pisano period.
    2. Find the remainder of n when divided by the length of the pisano period of m.
    3. Compute fibonacci number of the remainder.
    4. Compute F(remainder) % m
    
Example: F 2019 mod 5
    1. Find the length of the pisano period of 5 -->  length 20 https://en.wikipedia.org/wiki/Pisano_period
    2. Find the remainder of 2019 when divided by the length of the pisano period of 5.
        2019 % 20 = 19
    3. F(19)
    4. F(19) mod 5 = 1
        
:param: n <int> - Fn
:param: m <int> -
"""


def fibonacci_number_again(n: int, m: int) -> int:
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    # Get the length of the pisano period for m
    pisano_length = get_pisano_period_length(m)

    remainder = n % pisano_length

    # create an array of F[0...n]
    fib_list = [0, 1]

    # Calculate fibonacci number of the remainder (F remainder)
    for i in range(2, remainder + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list[remainder] % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))

# python3
"""
File name: fibonacci_number.py
Author: Sayuri Monarrez Yesaki
Date created: 10/25/2021
Date last modified: 10/25/2021
Python version: 3.8

Background: Fibonacci numbers is a fairly classical studied sequence of natural numbers. The 0th elements of the
sequence is 0; The 1st element of the sequence is 1; From thereon, each element is the sum of the previous two
elements.
        E.g. 0 1 1 2 3 5 8 13...
Use cases: mathematical model to study rabbit populations.

Problem: Implement an efficient algorithm for computing Fibonacci numbers.

Input: An integer n.

Output: Output Fn.
"""

"""
This naive algorithm was provided by the instructors; comments and descriptions were added by me.

Recursive algorithm to find fibonacci number.
Running time:
    If n at most 1: T  (n) = 2 lines of code.
    If n at least 2: T (n) = 3 + T(n - 1) + T ( n - 2)

    Therefore, T(n) >= Fn --> T(n) must get very very large, just like the fibonacci numbers.
    T(100) ~ 1.77 x 10 ^ 21 --> 56,000 years at 1GHz.

Computes the same thing over and over again -> very slow.

:param: n <int> - fibonacci number to compute
"""


def fibonacci_number_naive(n: int) -> int:
    assert 0 <= n <= 45
    # Base cases - If n <= 1 ( 0th or 1th), return n.
    if n <= 1:
        return n
    # Else, recursively calculate the sum of n - 1 plus n - 2.
    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


"""
Algorithm to compute the nth fibonacci number of Fn. 
Running time: 
    T(n) = 2n + 2
    T(100) = 202 lines of code to run.

:param: n - fibonacci number to compute
"""


def fibonacci_number(n: int) -> int:
    assert 0 <= n <= 45

    # create an array of F[0...n]
    fib_list = [0, 1]

    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

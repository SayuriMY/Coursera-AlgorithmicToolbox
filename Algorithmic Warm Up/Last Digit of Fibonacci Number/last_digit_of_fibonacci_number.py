# python3
"""
File name: last_digit_of_fibonacci_number.py
Author: Sayuri Monarrez Yesaki
Date created: 10/25/2021
Date last modified: 10/25/2021
Python version: 3.8

Background: Fibonacci numbers is a fairly classical studied sequence of natural numbers. The 0th elements of the
sequence is 0; The 1st element of the sequence is 1; From thereon, each element is the sum of the previous two
elements.
        E.g. 0 1 1 2 3 5 8 13...
Use cases: mathematical model to study rabbit populations.

Problem: Find the last digit of n-th Fibonacci number.

Hint: Store the last digit (Fi % 10) instead of the fibonacci number itself. To compute the last digit of a fibonacci
number just get the last digit of the sum of the last two digits of Fi-1 and Fi -2.

Input: An integer n.

Output: Output the last digit of Fn.
"""


"""
This naive algorithm was provided by the instructors.

Recursive algorithm to find the last digit of a fibonacci number.

:param: n <int> - fibonacci number to compute
"""


def last_digit_of_fibonacci_number_naive(n: int) -> int:
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


"""
Algorithm to compute the last digit of the nth fibonacci number of Fn. 
This algorithm stores the last digit of a fibonacci number instead of the fibonacci number itself. 
To compute the last digit of the next fibonacci number, sum the last digit of n - 1 and n - 2 and 
use modulus 10 to get the last digit of nth next fibonacci number.

:param: n - last digits of the nth fibonacci number
"""


def last_digit_of_fibonacci_number(n: int) -> int:
    assert 0 <= n <= 10 ** 7

    # create an array of last digits of F[0...n]
    fib_last_dig_list = [0, 1]

    for i in range(2, n + 1):
        last_digit = (fib_last_dig_list[i - 1] + fib_last_dig_list[i - 2]) % 10
        fib_last_dig_list.append(last_digit)

    return fib_last_dig_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))

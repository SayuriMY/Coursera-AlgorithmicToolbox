"""
File name: max_pairwise_product.py
Author: Sayuri Monarrez
Date created: 10/25/2021
Date last modified: 10/25/2021
Python version: 3.8

Problem: Given a sequence of non-negative int, find the max pairwise product, that is, max ai aj.

Input: First line of the input contains number 2 <= n <, 2 X 10 ^ 5. The next line contains n non-negative ints.

Output: Output a single number - the maximum pairwise product.
"""

''''
This implementation was provided by the course instructors as the naive solution.
'''


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    # initialize variable max_product - result
    # Note - potential issues:
    #    - integer overflow problem when using other programming languages such as C++
    #    - run time error ; takes mores than 1 sec (allowed time)
    product = 0
    # nested loop to test all possible combinations to find max pairwise product
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


"""
Find the maximum number by scanning the input array two times to find the two max numbers

:param 1: numbers - list of integers 
"""


def max_pairwise_product(numbers: list) -> int:
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    len_num = len(numbers)
    max_idx1 = -1
    for i in range(0, len_num):
        if (max_idx1 == -1) or numbers[i] > numbers[max_idx1]:
            max_idx1 = i

    max_idx2 = -1
    for j in range(0, len_num):
        if (j != max_idx1) and ((max_idx2 == -1) or (numbers[j] > numbers[max_idx2])):
            max_idx2 = j

    return numbers[max_idx1] * numbers[max_idx2]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))

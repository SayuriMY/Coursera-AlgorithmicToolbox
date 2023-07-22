# python3
"""
File name: number_of_inversions.py
Author: Sayuri Monarrez Yesaki
Date created: 12/29/2021
Date last modified: 03/28/2022
Python version: 3.8

Number of Inversions is one of the homework problems from week 4, Divide and Conquer Algorithms, of the Algorithmic
Toolbox course.

Task: count the number of inversions of a given sequence.

Input: The first line contains an integer n, the next one contains a sequence of integers a0, a1, ..., an-1.

Constraints: Output the number of inversions in the sequence.

Output:
"""
from itertools import combinations

'''
This naive solution was provided by the course instructors.
The runtime of this algorithm is quadratic O ( n ^2 ).
'''


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


'''

'''


# TODO
def compute_inversions(array_a: list):
    sorted_array, num_inversions = merge_sort(array_a)
    return num_inversions


def merge_sort(array_a: list):  # [9, 2, 9 ]
    n = len(array_a)  # 5
    # if the array len is 1, nothing needs to be done. The
    # array is already sorted.
    if n <= 1:
        return array_a, 0

    # Split the array into roughly two equal parts to sort
    # them recursively.
    m = n // 2  # 2
    array_b, inv_b = merge_sort(array_a[:m])
    array_c, inv_c = merge_sort(array_a[m:])
    # merge the two sub-arrays
    sorted_array, sorted_inv = merge(array_b, array_c)
    number_inversions = inv_b + inv_c + sorted_inv
    return sorted_array, number_inversions


'''
'''


# TODO
def merge(array_b: list, array_c: list) -> (list, int):
    array_d = []
    # number of pairs such that b > c
    num_inversions = 0
    while len(array_b) != 0 and len(array_c) != 0:
        b = array_b[0]
        c = array_c[0]
        if b <= c:
            array_d.append(array_b.pop(0))
        else:
            num_inversions += 1
            array_d.append(array_c.pop(0))
    if len(array_b) != 0:
        array_d.extend(array_b)
    else:
        array_d.extend(array_c)

    return array_d, num_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))

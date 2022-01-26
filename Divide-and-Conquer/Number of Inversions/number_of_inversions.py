# python3
"""
File name: number_of_inversions.py
Author: Sayuri Monarrez Yesaki
Date created: 12/29/2021
Date last modified: 12/29/2021
Python version: 3.8

Number of Inversions is one of the homework problems from week 4, Divide and Conquer Algorithms, of the Algorithmic
Toolbox course.

Task:

Input:

Constraints:

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
    n = len(array_a)
    if n <= 1:
        return array_a

    m = n // 2
    array_b = compute_inversions(array_a[:m])
    array_c = compute_inversions(array_a[m:])
    sorted_array = merge(array_b, array_c)
    return sorted_array


'''
'''


# TODO
def merge(array_b: list, array_c: list) -> list:
    array_d = []
    num_inversions = 0
    while len(array_b) != 0 and len(array_c) != 0:
        b = array_b[0]
        c = array_c[0]
        if b <= c:
            array_d.append(array_b.pop(0))
        else:
            array_d.append(array_c.pop(0))
    if len(array_b) != 0:
        array_d.extend(array_b)
    else:
        array_d.extend(array_c)
    return array_d


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))

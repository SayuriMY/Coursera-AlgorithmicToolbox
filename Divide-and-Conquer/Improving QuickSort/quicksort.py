# python3
"""
File name: quicksort.py
Author: Sayuri Monarrez Yesaki
Date created: 12/29/2021
Date last modified: 12/29/2021
Python version: 3.8

Quicksort is one of the homework problems from week 4, Divide and Conquer Algorithms, of the Algorithmic Toolbox course.

Task: To force the given implementation of the quick sort algorithm to efficiently process sequences with few unique
elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new partition procedure should
partition the array into three parts: < x part, = x part, > x part.

Input: The first line of the input contains an integer 𝑛. The next line contains a sequence of 𝑛
integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.

Constraints: 1 ≤ 𝑛 ≤ 10^5 ; 0 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.

Output: Output this sequence sorted in non-decreasing order.
"""

from random import randint

'''
My solution to the problem

Partition3 method is based on "Sort and array of 0s, 1s, and 2" 
from https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

The array is divided into three sections:
1. array[left...m1-1]
2. array[m1...m2]
3. array[m2+1...right]

If the ith element is less than x (pivot) then swap the element to the low range.
Similarly, if the element is equal to x (pivot) then swap the element to the mid range.
If the element is greater than x (pivot) then swap the element to the high range.

Algorithm:
- Keep indices m1, m2, i, left, and right and there are three ranges: 
left to m1 ( elements < x), m1 to m2 ( elements  == x), and  m2 to right (element > x).
- Traverse the array from left to right; i is less than right.
- If the element is less than x, swap the element at index m1. Increment
m1 and m2 by 1 position.
- If the element is equal to x, increment m2 by 1. Swap m2 and the ith element.
- If the element is greater than x, swap the element with the element at index right. 
Decrease the right and i indices by 1.
'''


def partition3(array: list, left: int, right: int) -> (int, int):
    # pivot element
    x = array[left]
    m1 = left
    m2 = left
    i = left + 1
    while i <= right:
        if array[i] < x:
            array[m1], array[i] = array[i], array[m1]
            m1 += 1
            m2 += 1
        elif array[i] == x:
            m2 += 1
            array[m2], array[i] = array[i], array[m2]
        else:
            array[right], array[i] = array[i], array[right]
            right -= 1
            i -= 1
        i += 1
    return m1, m2


def randomized_quick_sort(array: list, left: int, right: int) -> None:
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    '''My solution to the problem starts here'''
    (m1, m2) = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

"""
File name: binary_search.py
Author: Sayuri Monarrez Yesaki
Date created: 11/23/2021
Date last modified: 11/23/2021
Python version: 3.8

Binary Search is one of the homework problems from week 4, Divide and Conquer Algorithms, of the Algorithmic Toolbox
course.

Binary Search is an efficient algorithm for finding an item from a sorted list of items.

Task: Implement binary search

Input: The first line of the input contains an integer 𝑛 and a sequence 𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1 of 𝑛 pairwise distinct
    positive integers in increasing order. The next line contains an integer 𝑘 and 𝑘 positive integers
    𝑏0, 𝑏1, . . . , 𝑏𝑘−1.

Constraints: 1≤𝑛,𝑘≤104;1≤𝑎𝑖 ≤109 for all 0≤𝑖<𝑛;1≤𝑏𝑗 ≤109 for all 0≤𝑗<𝑘;

Output: For all 𝑖 from 0 to 𝑘−1, output an index 0≤𝑗≤𝑛−1 such that 𝑎𝑗 =𝑏𝑖 or −1 if there is no such index.
"""

''''
This solution was provided by the course instructors.
'''


def linear_search(keys: list, query: int) -> int:
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


''''
Given the sorted array of elements, keys, search for the given element, query, in the array
or return -1 if not found.
'''


def binary_search(keys: list, query: int) -> int:
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    return binary_search_iterative_helper(keys, 0, len(keys) - 1, query)


''''
Iterative algorithms that searches the sorted_array by repeatedly dividing the search in half. 
It starts covering the whole array. If the value of "key" is higher than the item in the middle element
of the interval, narrow the interval to the upper half. Otherwise, narrow it to the lower half. Continue 
the search while the key hasn't been found and the low interval is lower or equal to the high interval.
'''


def binary_search_iterative_helper(sorted_array: list, low: int, high: int, key: int) -> int:
    while low <= high:
        mid = ((high - low) // 2) + low

        if key == sorted_array[mid]:
            return mid
        elif sorted_array[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

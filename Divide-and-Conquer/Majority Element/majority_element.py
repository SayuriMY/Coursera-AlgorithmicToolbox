"""
File name: majority_element.py
Author: Sayuri Monarrez Yesaki
Date created: 11/24/2021
Date last modified: 12/28/2021
Python version: 3.8

Majority Element is one of the homework problems from week 4, Divide and Conquer Algorithms, of the Algorithmic Toolbox course.

The Majority rule is a decision rule that selects the alternative which has a majority, that is, more than half the votes.
Given a sequence of elements, check whether it contains an element that appears more than n/2 times.

Task: Use divide an conquer technique to design an O ( n log n ) algorithm to check whether an input sequence contains
a majority element.

Input: The first line contains an integer n, the next contains a sequence of n non-negative integers.

Constraints: 1 ≤ 𝑛 ≤ 10^5 ; 0 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.

Output: Output 1 if the sequence contains an element that appears strictly more than n/2 times, and 0 otherwise.
"""

'''
This naive solution was provided by the course instructors.
The runtime of this algorithm is quadratic O ( n ^2 ).
'''


def majority_element_naive(elements: list) -> int:
    assert len(elements) <= 10 ** 5
    for e in elements:
        # count() method returns the number of elements with the specified value.
        # O( n ) runtime --> need to check all elements in the list.
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


'''
Non-divide and conquer approach.
Running time: O(n)
This algorithm scans the sequence twice and returns 1 if there is a majority element, 
0 otherwise.

The majority rule states that an element appears more then half the elements 
in the given array.
    E.g. [ 2, 3, 9, 2, 2 ]
        
         length: 5
         majority element: 2, it appears 3 times in the array
'''


def majority_element(elements: list) -> int:
    assert len(elements) <= 10 ** 5
    threshold = len(elements) // 2
    elements_map = dict()

    for element in elements:
        count = elements_map.get(element, 0)
        elements_map[element] = count + 1

    for element in elements_map:
        if elements_map[element] > threshold:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))

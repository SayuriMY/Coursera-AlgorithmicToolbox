# python3
"""
File name: primitive_calculator.py
Author: Sayuri Monarrez Yesaki
Date created: 01/05/2022
Date last modified: 01/05/2022
Python version: 3.8

Primitive Calculator is one of the homework problems from week 5, Dynamic Programming Algorithms, of the Algorithmic
Toolbox course.

The primitive calculator being used can perform the following three operations with the current number x:
multiply x by 2, multiply x by 3, or add 1 to x. Find the minimum number of operations needed to obtain the
number n starting from the number 1.

Task: Given an integer n, compute the minimum number of operation needed to obtain the number n starting
from the number 1.

Input: A single integer 1 <= n <= 10^6

Constraints:

Output: In the first line, output the minimum number k of operations needed to get n from 1. In the second line, output
a sequence of intermediate numbers. That is, the second line should contain positive integers a0, a1, ... ak-1 such that
a1 = 1, ak-1 = n and for all 0 <= i < k - 1, ai+1 is equal to either ai + 1, 2ai, or 3ai. If there are many such
sequences, output any of them
"""
import copy
import math

'''
My solution to the problem

In this approach, the array computed_values is being filled out from left to right from 0 to n.

The min number of operations needed to get 0, is zero. Continue iterating  from 1 to n. 

For each value val, compute the minimum number of operations needed to obtain val, where only +1, x2, and x3 
operations are allowed.

For each val:
1. Compute number of operations if the next operation was +1, add_1.
2. If val is a multiple of 2, compute the number of operations if the next op was x2, mult_2.
3. If val is a multiple of 3, compute the num of operations if the next op was x3, mult_3.
4. Find the minimum number of operations between add_1, mult_2, and mult_3.
5. Deep copy the list at the idx based on the selected operation, append val. Append 
new_list to coputed_values.

Runtime: O(n)
Space complexity:
'''


def compute_operations(n: int) -> int:
    assert 1 <= n <= 10 ** 6
    # Initialize the array by entering the minimum number of coins needed to change
    # zero money.
    computed_values = [[]]

    # iterate over 1 to n
    # range(start, end) is not inclusive -> +1 to make sure money is processed
    for val in range(1, n + 1):

        # check +1
        # Add +1 coin to the previously calculated value of min_num_operations[ val - 1]
        add_1 = len(computed_values[val - 1]) - 1 + 1

        # check x2
        mult_2 = math.inf
        if (val % 2) == 0:
            mult_2 = len(computed_values[val // 2]) - 1 + 1

        # check x3
        mult_3 = math.inf
        if (val % 3) == 0:
            mult_3 = len(computed_values[val // 3]) - 1 + 1

        num_operations = min(add_1, mult_2, mult_3)

        idx = val - 1
        if num_operations == mult_2:
            idx = val // 2
        elif num_operations == mult_3:
            idx = val // 3

        new_list = copy.deepcopy(computed_values[idx])
        new_list.append(val)
        computed_values.append(new_list)

    return computed_values[n]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)

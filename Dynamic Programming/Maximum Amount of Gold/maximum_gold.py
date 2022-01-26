# python3
"""
File name: maximum_gold.py
Author: Sayuri Monarrez Yesaki
Date created: 01/11/2022
Date last modified: 01/11/2022
Python version: 3.8

Maximum gold is one of the homework problems from week 6, Dynamic Programming Algorithms, of the Algorithmic
Toolbox course.

You are given a set of bars of gold and your goal is to take as much gold as possible into your bag.
there is just one copy of each bar and for each bar you can either take it or not
( hence you cannot take a fraction of a bar).

Task: Given n gold bars, find the maximum weight of gold that firts into a bag of capacity W.

Input: The first line of the input contains the capacity W of a knapsack and the number n of bars of gold.
The next line contains n integers w0, w1, ..., wn-1 defining the weights of the bars of gold.

Constraints:  1 ≤ 𝑊 ≤ 104 ; 1 ≤ 𝑛 ≤ 300; 0 ≤ 𝑤0, . . . , 𝑤𝑛−1 ≤ 105

Output: Output the maximum weight of gold that fits into a knapsack of capacity W.
"""
from sys import stdin

""""

"""
# TODO: Fix bug in the algorithm. The algorithm fills the rows before the last one incorrectly.

def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    '''My solution to the problem starts here.'''
    maximum_gold_matrix = []
    for w in range(len(weights) + 1):
        n = [0] * (capacity + 1)
        maximum_gold_matrix.append(n)

    for i in range(1, len(weights) + 1):  # rows
        for w in range(1, capacity + 1):  # columns
            # compute the value of w and i - 1
            maximum_gold_matrix[i][w] = maximum_gold_matrix[i - 1][w]

            if weights[i - 1] <= w:
                val = maximum_gold_matrix[i - 1][w - weights[i - 1]] + weights[i - 1]

                if maximum_gold_matrix[i][w] < val:
                    maximum_gold_matrix[i][w] = val

    return maximum_gold_matrix[len(weights)][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))

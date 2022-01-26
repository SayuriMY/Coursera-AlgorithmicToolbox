# python3
"""
File name: maximum_ad_revenue.py
Author: Sayuri Monarrez Yesaki
Date created: 11/22/2021
Date last modified: 11/22/2021
Python version: 3.8

Maximum Advertisement Revenue or "Dot Product" is one of the homework problems from week 3, Greedy Algorithms,
of the Algorithmic Toolbox course.

You have 𝑛 ads to place on a popular Internet page. For each ad, you know how much is the advertiser willing to pay
 for one click on this ad. You have set up 𝑛 slots on your page and estimated the expected number of clicks per day
 for each slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue.

Task: Given two sequences 𝑎1,𝑎2,...,𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1,𝑏2,...,𝑏𝑛
(𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎𝑖,𝑏𝑗) such
that the sum of their products is maximized.

Input: The first line contains an integer 𝑛, the second one contains a sequence of integers 𝑎1,𝑎2,...,𝑎𝑛,
the third one contains a sequence of integers 𝑏1,𝑏2,...,𝑏𝑛.

Constraints: 1≤𝑛≤103;−105 ≤𝑎𝑖,𝑏𝑖 ≤105 forall1≤𝑖≤𝑛.

Output: Output the maximum value of ∑︀ 𝑎𝑖𝑐𝑖, where 𝑐1, 𝑐2, . . . , 𝑐𝑛 is a permutation of 𝑏1,𝑏2,...,𝑏𝑛.
"""
from itertools import permutations

"""
This naive algorithm was provided by the instructors.
"""


def max_dot_product_naive(first_sequence: list, second_sequence: list) -> int:
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


"""
First, sort the first and second sequences in descending order. Then, iterate over the
sequences, calculate the product, add the product of the ith elements. Finally, return the
maximum revenue. 
"""


def max_dot_product(first_sequence: list, second_sequence: list) -> int:
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3

    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)

    max_revenue = 0

    for i in range(len(first_sequence)):
        max_revenue += first_sequence[i] * second_sequence[i]
    return max_revenue


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))

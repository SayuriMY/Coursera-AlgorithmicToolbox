# python3
"""
File name: maximum_number_of_prizes.py
Author: Sayuri Monarrez Yesaki
Date created: 01/18/2022
Date last modified: 01/18/2022
Python version: 3.8

Maximum number of prizes  is one of the homework problems from week 3, Greedy Algorithms,
of the Algorithmic Toolbox course.

You are organizing a funny competition for children. As a prize fund you have π
candies. You would like to use these candies for top π places in a competition
with a natural restriction that a higher place gets a larger number of candies.
To make as many children happy as possible, you are going to find the largest
value of π for which it is possible

Task: The goal of this problem is to represent a given positive integer π as a sum of as many pairwise
distinct positive integers as possible. That is, to find the maximum π such that π can be written as
π1 + π2 + Β· Β· Β· + ππ where π1, . . . , ππ are positive integers and ππ ΜΈ= ππ for all 1 β€ π < π β€ οΏ½

Input: Single integer n.

Constraints: 1 <= n <= 10 ^9

Output:  In the first line, output the maximum number π such that π can be represented as a sum
of π pairwise distinct positive integers. In the second line, output π pairwise distinct positive integers
that sum up to π (if there are many such representations, output any of them).
"""


def compute_optimal_summands(n: int) -> list:
    assert 1 <= n <= 10 ** 9
    summands = []
    total_sum = 0
    i = 1
    rest = n
    while total_sum < n and rest >= i:
        summands.append(i)
        total_sum += i
        rest -= i
        i += 1
    summands[i - 2] = summands[i - 2] + rest

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)

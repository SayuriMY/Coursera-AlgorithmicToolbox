# python3
"""
File name: maximum_number_of_prizes.py
Author: Sayuri Monarrez Yesaki
Date created: 01/18/2022
Date last modified: 01/18/2022
Python version: 3.8

Maximum number of prizes  is one of the homework problems from week 3, Greedy Algorithms,
of the Algorithmic Toolbox course.

You are organizing a funny competition for children. As a prize fund you have 𝑛
candies. You would like to use these candies for top 𝑘 places in a competition
with a natural restriction that a higher place gets a larger number of candies.
To make as many children happy as possible, you are going to find the largest
value of 𝑘 for which it is possible

Task: The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise
distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as
𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 ̸= 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ �

Input: Single integer n.

Constraints: 1 <= n <= 10 ^9

Output:  In the first line, output the maximum number 𝑘 such that 𝑛 can be represented as a sum
of 𝑘 pairwise distinct positive integers. In the second line, output 𝑘 pairwise distinct positive integers
that sum up to 𝑛 (if there are many such representations, output any of them).
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

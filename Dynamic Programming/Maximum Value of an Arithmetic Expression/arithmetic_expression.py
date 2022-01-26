# python3
"""
File name: arithmetic_expression.py
Author: Sayuri Monarrez Yesaki
Date created: 01/12/2022
Date last modified: 01/12/2022
Python version: 3.8

Arithmetic expression is one of the homework problems from week 6, Dynamic Programming Algorithms, of the Algorithmic
Toolbox course.

In this problem, your goal is to add parentheses to a given arithmetic expression to maximize its value.

Task: Fin the maximum value of an arithmetic expression by specifying the order of applying its arithmetic operations
using additional parentheses.

Input: String s of length 2n + 1 for some n, with symbols s0, s1, ..., s2n. Each symbol at an even position of s is a
digit ( that is, an integer from 0 to 9) while each symbol at an odd position is one of the three operations from
{ +, -, *}.

Constraints:  1 ≤ 𝑛 ≤ 14 (hence the string contains at most 29 symbols).

Output: Output the maximum possible value of the given arithmetic expression among different orders of applying
arithmetic operations.
"""
import copy
import math
import operator


def min_and_max(i: int, j: int, min_matrix: list, max_matrix: list, operators: list) -> (int, int):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    # Declare min and max values.
    min_val = math.inf
    max_val = -math.inf

    for k in range(i, j):
        a = ops[operators[k - 1]](max_matrix[i - 1][k - 1], max_matrix[k][j - 1])
        b = ops[operators[k - 1]](max_matrix[i - 1][k - 1], min_matrix[k][j - 1])
        c = ops[operators[k - 1]](min_matrix[i - 1][k - 1], max_matrix[k][j - 1])
        d = ops[operators[k - 1]](min_matrix[i - 1][k - 1], min_matrix[k][j - 1])

        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)

    return min_val, max_val


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    n = (len(dataset) + 1) // 2

    # Two matrices need to be maintained: min values and max values.
    # Initialize matrices of zeros.
    matrix_min = []
    matrix_max = []
    for i in range(n):
        row = [0] * n
        row[i] = int(dataset[2 * i])
        matrix_min.append(copy.deepcopy(row))
        matrix_max.append(copy.deepcopy(row))

    operators = []
    for i in range(len(dataset)):
        if i % 2 != 0:
            operators.append(dataset[i])

    # Iterate over all possible subproblems in order of increasing size.
    for sub in range(1, n):
        # When sub is fixed, i goes through 1 to n - sub
        for i in range(1, n - sub + 1):
            j = i + sub
            matrix_min[i - 1][j - 1], matrix_max[i - 1][j - 1] = min_and_max(i, j, matrix_min, matrix_max, operators)

    return matrix_max[0][n - 1]


if __name__ == "__main__":
    print(find_maximum_value(input()))

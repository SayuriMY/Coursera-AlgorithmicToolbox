# python3
"""
File name: money_change.py
Author: Sayuri Monarrez Yesaki
Date created: 11/17/2021
Date last modified: 11/17/2021
Python version: 3.8

Money Change is one of the homework problems from week 3, Greedy Algorithms, of the Algorithmic Toolbox course.

Task: Find the minimum number of coins needed to change the input value (an int) into coins with denominations 1, 5,
and 10.

Input: single integer m.

Constraints: 1 <= m <= 10^3.

Output: Minimum number of coins with denominations 1, 5, 10 that changes m.

Example 1:
    input: 2

    1 + 1 = 2

    Output: 2
"""

""""
This algorithm finds the min number of coins needed to change the given money into coins with
denominations 1, 5, and 10.
Algorithm:
1. Find max. number of coins with denomination 10.
2. Subtract # coins x 10 from input value.
3. Repeat for coins with denominations 5 and 1 until change equals input value.

:param: money <int> 
"""


def money_change(money: int) -> int:
    assert 0 <= money <= 10 ** 3
    change = money

    denominations = [10, 5, 1]
    min_num_coins = 0

    for den in denominations:
        if change != 0:
            # Get the minimum number of coins of denomination den could be used  to give change.
            min_num = change // den

            # Subtract the quantity of the change that has been accounted for in the previous step.
            change = change - min_num * den

            min_num_coins += min_num

    return min_num_coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))

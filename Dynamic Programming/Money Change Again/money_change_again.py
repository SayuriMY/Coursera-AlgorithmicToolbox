# python3
"""
File name: money_change_again.py
Author: Sayuri Monarrez Yesaki
Date created: 01/05/2022
Date last modified: 01/05/2022
Python version: 3.8

Money Change Again is one of the homework problems from week 5, Dynamic Programming Algorithms, of the Algorithmic
Toolbox course.

Task: Apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.

Input: Integer money.

Constraints: 1 <= money <= 10^3

Output: The minimum number of coins with denominations 1, 3, 4 that changes money.
"""
import math

'''
This naive solution was provided by the course instructors.
'''


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


'''
My solution to the problem

This algorithm was covered in one of the video lectures of the Algorithmic
Toolbox course. 

In this approach, the array min_num_coins is being filled out from left to right
from 0 to money.

The min number of coins needed to change 0 money, is zero. Continue iterating 
from 1 to money. 
For each money m, compute the minimum number of coins needed of 
denominations 1, 3, and/or 4.
For each m:
1. Initialize min_num_coins[ m ] to infinity.
2. For each coin denomination, where m >= coin, compute the minimum number of coins
needed based on a previously calculated value.

Runtime: O ( coins * money)
Space complexity: O( money )
'''


def change(money: int) -> int:
    # Initialize the array by entering the minimum number of coins needed to change
    # zero money.
    min_num_coins = [0]

    # iterate over 1 to money
    # range(start, end) is not inclusive -> +1 to make sure money is processed
    for m in range(1, money + 1):
        # set up min_num_coins  for m as infinity.
        min_num_coins.append(math.inf)
        for coin in [1, 3, 4]:
            if m >= coin:
                # Add +1 coin to the previously calculated value of min_num_coins[m - coin]
                num_coins = min_num_coins[m - coin] + 1
                # If num_coins is less than the saved min_num_coins, update min_cun_coins
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))

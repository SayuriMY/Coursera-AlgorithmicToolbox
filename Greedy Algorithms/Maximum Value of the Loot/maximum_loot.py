# python3
"""
File name: fractional_knapsack.py
Author: Sayuri Monarrez Yesaki
Date created: 11/17/2021
Date last modified: 11/17/2021
Python version: 3.8

"Maximum Value of the Loot" or Fractional Knapsack is one of the homework problems from week 3,
Greedy Algorithms, of the Algorithmic Toolbox course.

Task: The goal of this problem is to implement an algorithm for the fractional knapsack problem.

Input: The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
       The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value
       and the weight of 𝑖-th item, respectively.

Constraints: 1≤𝑛≤103,0≤𝑊 ≤2·106;0≤𝑣𝑖 ≤2·106,0<𝑤𝑖 ≤2·106 for all 1≤𝑖≤𝑛. All the numbers are integers.

Output: Output the maximal value of fractions of items that fit into the knapsack. The absolute value of the difference
        between the answer of your program and the optimal value should be at most 10^−3. To ensure this, output your
        answer with at least four digits after the decimal point.
"""

from sys import stdin
import copy

"""
Calculates fractions based on weights and values. Then, it sorts
the fractions in descending order.

:param: weights <list[int]> 
:param: values <list[int]> 
"""


def order_fraction_descending(weights: list, values: list) -> (list, list):
    fractions = []

    # calculate fractions based on weights and values
    for i in range(len(weights)):
        fractions.append(values[i] / weights[i])

    # Sort fractions in descending order.
    fractions_descending = copy.deepcopy(fractions)
    fractions_descending.sort(reverse=True)

    return fractions, fractions_descending


"""
Calculates the optimal combination of items assuming that any fraction of 
an item can be put into the knapsack.

Iterate over the fractions, if the knapsack is full return the optimal
value; else, find the idx of the highest fraction that has not been used, 
if the item fits into the knapsack take all of it
otherwise, take so much as to fill the knapsack.
update the optimal value of the knapsack and the capacity
return optimal value.

:param: capacity <int> capacity of the knapsack
:param: weights <list[int]> weights of items
:param: prices <list[int]>  values or prices of items
"""


def maximum_loot_value(capacity: int, weights: list, prices: list) -> float:
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    optimal_value = 0

    # Get fractions and ordered fractions in descending order
    fractions, fractions_desc = order_fraction_descending(weights, prices)

    # Iterate over fractions in descending order.
    for fraction in fractions_desc:
        if capacity == 0:  # Knapsack already full
            return optimal_value

        # Get the index of the highest fraction that has not been used.
        idx = fractions.index(fraction)

        # Find minimum between capacity and weight of the given item.
        a = min(capacity, weights[idx])

        # Update variables
        optimal_value = optimal_value + (a * fraction)
        capacity -= a

    return optimal_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))

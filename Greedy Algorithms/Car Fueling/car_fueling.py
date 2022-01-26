# python3
"""
File name: car_fueling.py
Author: Sayuri Monarrez Yesaki
Date created: 11/22/2021
Date last modified: 01/18/2022
Python version: 3.8

Car fueling is one of the homework problems from week 3, Greedy Algorithms, of the Algorithmic Toolbox course.

You are going to travel to another city that is located d miles away from your home city. Your car can travel at most
m miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances stop1, stop2,
..., stopn form your home city. What is the minimum number of refills needed?

Task: Determine the number of refills needed to travel from another city located a d miles away from your home city.

Input: First line contains an integer d. The second line contains an integer m. The third line specifies an integer n.
Finally, the last line contains integers stop1, stop2, ..., stopn.

Constraints: 1≤𝑑≤10 .1≤𝑚≤400.1≤𝑛≤300.0<stop1 <stop2 <···<stop𝑛 <𝑚.

Output: Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles on a full tank,
        and there are gas stations at distances stop1 , stop2 , . . . , stop𝑛 along the way,
        output the minimum number of refills needed.
        Assume that the car starts with a full tank. If it is not possible to reach the destination, output −1.

"""

"""
Computes the minimum number of tank refills needed to arrive
from origin to distance d if the car can travel at most m miles.

Running time: O ( n )

:param: d <int> distance 
:param: m <int> miles 
:param: stops <list[int]> positions of the gas stations
"""


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    # number of refills we have already made.
    # at idx 0, we have not made any refills yet.
    num_refills = 0
    # index where we're currently standing
    current_refill = 0

    # add starting position, 0, and destination, d, into the stops array.
    stops.insert(0, 0)
    stops.append(d)

    while current_refill < len(stops) - 1:
        # the last refill was made at the current_refill idx
        last_refill = current_refill

        # either get to destination or get to the right most reachable station and refill there.
        # current_refill <= len(stops) ---> we have reached destination
        # ((stops[current_refill + 1] - stops[last_refill]) <= m) ---> look at the next position
        # to the right and check if it's reachable from the last refill position or not.
        while (current_refill < len(stops) - 1) \
                and ((stops[current_refill + 1] - stops[last_refill]) <= m):
            current_refill += 1

        # not enough fuel to get to the next gas station
        if current_refill == last_refill:
            return -1
        elif current_refill < len(stops) - 1:
            num_refills += 1

    return num_refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))

# python3
"""
File name: collecting_signatures.py
Author: Sayuri Monarrez Yesaki
Date created: 11/22/2021
Date last modified: 01/18/2022
Python version: 3.8

Collecting Signatures or "covering segments" is one of the homework problems from week 3, Greedy Algorithms,
of the Algorithmic Toolbox course.

You are responsible for collecting signatures from all tenants of a certain building. For each tenant, you know a
period of time when he or she is at home. You would like to collect all signatures by visiting the building as few
times as possible.

Mathematical Model:
You are given a set of segments on a line and your goal is to mark as few points on a line as possible so that each
segment contains at least one marked point.

Task: Given a set of 𝑛 segments {[𝑎0,𝑏0],[𝑎1,𝑏1],...,[𝑎𝑛−1,𝑏𝑛−1]} with integer coordinates on a line, find the minimum
number 𝑚 of points such that each segment contains at least one point. That is, find a set of integers 𝑋 of the minimum
 size such that for any segment [𝑎𝑖,𝑏𝑖] there is a point 𝑥 ∈ 𝑋 such that𝑎𝑖 ≤𝑥≤𝑏𝑖.

Input: The first line of the input contains the number 𝑛 of segments. Each of the following 𝑛 lines contains two
integers 𝑎𝑖 and 𝑏𝑖 (separated by a space) defining the coordinates of endpoints of the 𝑖-th segment.

Constraints: 1≤𝑛≤100;0≤𝑎𝑖 ≤𝑏𝑖 ≤109 forall0≤𝑖<𝑛.

Output: Output the minimum number 𝑚 of points on the first line and the integer coordinates of 𝑚 points (separated by
spaces) on the second line. You can output the points in any order. If there are many such sets of points, you can
output any set. (It is not difficult to see that there always exist a set of points of the minimum size such that all
the coordinates of the points are integers.)

"""
from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

'''
Finds the minimum number of points such that each segment contains at least one point.

:param: segments <list> list of namedtuple representing
the segments. 
'''


def compute_optimal_points(segments: list) -> list:
    segments.sort()

    optimal_points = []
    current_opt_start = segments[0].start
    current_opt_end = segments[0].end

    for i in range(1, len(segments)):
        # if the next segment does NOT overlap with current_opt_segment, save a point in optimal points
        # update current_opt_start and current_opt_end values to the start and end of the ith segment.
        if segments[i].start > current_opt_end:
            optimal_points.append(current_opt_end)

            current_opt_start = segments[i].start
            current_opt_end = segments[i].end
        else:
            '''
            If necessary, update the current_opt start and end values to find the "optimal" start and end
            values after analyzing the ith segment.
                example: 
                            1   2   3   4   5   6
                            _________                   segment(1,3) --> current_opt_start = 1 ; current_opt_end = 3
                                _____________           segment(2,5)
                                
                Since the start of segment[i] > current_opt_start, update its value to segment[i].start. There is no
                need to update the end value since the current_opt_end is smaller than segment[i].end
                
                            1   2   3   4   5   6
                            _________                   segment(1,3) --> prev. current_opt_start = 1 ; current_opt_end = 3
                                _____________           segment(2,5)
                                _____                   updated values: current_opt_start = 2 ; current_opt_end = 3
            '''
            if current_opt_start < segments[i].start:
                current_opt_start = segments[i].start

            if current_opt_end > segments[i].end:
                current_opt_end = segments[i].end

    optimal_points.append(current_opt_end)

    return optimal_points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)

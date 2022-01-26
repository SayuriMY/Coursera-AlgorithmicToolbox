# python3
"""
File name: edit_distance.py
Author: Sayuri Monarrez Yesaki
Date created: 01/08/2022
Date last modified: 01/08/2022
Python version: 3.8

Edit Distance is one of the homework problems from week 5, Dynamic Programming Algorithms, of the Algorithmic
Toolbox course.

Task: Implement the algorithm for computing the edit distance between two strings.

Input: Each of the two lines of the input contains a string consisting of lower case latin letters.

Constraints: The length of both strings is at least 1 and at most 100.

Output: Output the edit distance between the given two strings.
"""

'''
My solution to the problem.

This algorithm was covered in one of the video lectures of the Algorithmic
Toolbox course. 
'''


def edit_distance(first_string: str, second_string: str) -> int:
    # create empty edit distance
    edit_dist_matrix = []
    for m in range(len(first_string) + 1):
        n = [0] * (len(second_string) + 1)
        edit_dist_matrix.append(n)

    # Enter values 0 to len(first_string) + 1 into the first column
    for i in range(len(first_string) + 1):
        edit_dist_matrix[i][0] = i

    # Enter values 0 to len(second_string) + 1 into the first row.
    for j in range(len(second_string) + 1):
        edit_dist_matrix[0][j] = j

    # Fill out the rest of the values in the edit_distance_matrix.
    for j in range(1, len(second_string) + 1):
        for i in range(1, len(first_string) + 1):
            insertion = edit_dist_matrix[i][j - 1] + 1
            deletion = edit_dist_matrix[i - 1][j] + 1
            match = edit_dist_matrix[i - 1][j - 1]
            mismatch = edit_dist_matrix[i - 1][j - 1] + 1

            if first_string[i - 1] == second_string[j - 1]:
                edit_dist_matrix[i][j] = min(insertion, deletion, match)
            else:
                edit_dist_matrix[i][j] = min(insertion, deletion, mismatch)

    return edit_dist_matrix[len(first_string)][len(second_string)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))

# python3
"""
File name: maximum_number_of_prizes.py
Author: Sayuri Monarrez Yesaki
Date created: 01/23/2022
Date last modified: 01/23/2022
Python version: 3.8

Maximum salary  is one of the homework problems from week 3, Greedy Algorithms,
of the Algorithmic Toolbox course.

Find the largest number consisting of the given digits.
During the course lectures, the following algorithm was used for composing the largest number out of the given
single-digit numbers.

LargestNumber(Digits):
answer <- empty string
while Digits is not empty:
    maxDigit <- -inf
    for digit in Digits:
        maxDigit <- digit
    append maxDigit to answer
    remove maxDigit from Digits
return answer

Task: Tweak the algorithm from the lecture so that it works not only for single-digit numbers, but for arbitrary
positive integers.

Input: The first line of the input contains an integer n. The second line contains integers a1, a2, ..., an.

Constraints: 1 <= n <= 100; 1 <= a1 <= 10 ^3 for all 1 <= i <= n

Output: Output the largest number that can be composed out of a1, a2, ..., an.
"""
from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


# TODO: There is a bug in this algorithm. It still does not pass all test cases when the assignment is submitted.
def num_is_larger_than_max(max_num: str, num: str) -> bool:
    if max_num.startswith(num):
        if max_num[len(num)] < num[0]:
            return True
        elif max_num[len(num)] == num[0] and (len(num) > 1 and max_num[len(num)] < num[1]):
            return True
        else:
            # elif max_num[len(num)] == num[0] and max_num[len(num)] > num[1] || max_num[len(num)] > num[0]
            return False

    length = min(len(max_num), len(num))
    for i in range(length):
        if num[i] > max_num[i]:
            return True
        return False
    return False


def largest_number(numbers: list) -> int:
    answer = ""
    numbers.sort(reverse=True)
    while len(numbers) > 0:
        max_num = numbers[0]
        for i in range(1, len(numbers)):
            if len(max_num) != len(numbers[i]):
                num_is_larger = num_is_larger_than_max(max_num, numbers[i])
                if num_is_larger:
                    max_num = numbers[i]
            elif numbers[i] >= max_num:
                max_num = numbers[i]
        answer = answer + max_num
        numbers.remove(max_num)
    return int(answer)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))

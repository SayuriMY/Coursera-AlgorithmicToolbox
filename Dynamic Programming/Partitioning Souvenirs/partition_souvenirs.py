# python3

from itertools import product
from sys import stdin


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    if len(values) < 3:
        return 0

    total_sum = sum(values)

    if total_sum % 3 != 0:
        return 0

    part_value = total_sum * (1 / 3)
    sum1 = sum2 = sum3 = part_value

    sorted(values)

    for i in range(len(values) - 1, -1, -1):
        if values[i] <= sum1:
            sum1 -= values[i]
        elif values[i] <= sum2:
            sum2 -= values[i]
        elif values[i] <= sum3:
            sum3 -= values[i]
        else:
            return 0

    if sum1 == 0 and sum2 == 0 and sum3 == 0:
        return 1

    return 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))

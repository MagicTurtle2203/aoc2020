from typing import Dict, List, Optional, Union


def part1(data: List[int]) -> int:
    data = [0] + (s := sorted(data)) + [s[-1] + 3]

    ones = 0
    threes = 0

    for i in range(1, len(data)):
        if data[i] - data[i - 1] == 1:
            ones += 1
        elif data[i] - data[i - 1] == 3:
            threes += 1

    return ones * threes


def helper(data: List[int], index: int, memo: List[int]) -> int:
    if len(data[index:]) == 1:
        return 1

    start = data[index]

    if memo[index] > 0:
        return memo[index]

    queue = []

    i = index + 1
    while i < len(data) and data[i] <= start + 3:
        queue.append(i)
        i += 1

    counts = 0
    for j in queue:
        counts += helper(data, j, memo)

    memo[index] = counts

    return counts


def part2(data: List[int]) -> int:
    data = [0] + (s := sorted(data)) + [s[-1] + 3]

    memo = [0 for _ in range(len(data) + 1)]

    return helper(data, 0, memo)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = list(map(int, file.read().splitlines()))
    print(part1(data))
    print(part2(data))

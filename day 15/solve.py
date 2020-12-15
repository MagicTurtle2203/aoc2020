from typing import Dict, List, Optional, Union


def part1(data: List[int]) -> int:
    d = {}

    turn_number = 1
    for turn_number, number in enumerate(data, 1):
        d[number] = turn_number

    n = data[-1]
    if n in d:
        difference = turn_number - d[n]
        d[n] = turn_number
        n = difference
    else:
        d[n] = turn_number
        n = 0
    turn_number += 1

    while turn_number != 2020:
        if n in d:
            difference = turn_number - d[n]
            d[n] = turn_number
            n = difference
        else:
            d[n] = turn_number
            n = 0
        turn_number += 1

    return n


def part2(data: List[int]) -> int:
    d = {}

    turn_number = 1
    for turn_number, number in enumerate(data, 1):
        d[number] = turn_number

    n = data[-1]
    if n in d:
        difference = turn_number - d[n]
        d[n] = turn_number
        n = difference
    else:
        d[n] = turn_number
        n = 0
    turn_number += 1

    while turn_number != 30000000:
        if n in d:
            difference = turn_number - d[n]
            d[n] = turn_number
            n = difference
        else:
            d[n] = turn_number
            n = 0
        turn_number += 1

    return n


if __name__ == "__main__":
    data = list(map(int, "2,20,0,4,1,17".split(",")))
    print(part1(data))
    print(part2(data))

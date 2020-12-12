from typing import List


def part1(inputs: List[str]) -> int:
    inputs = list(map(lambda x: x.replace("\n", ""), inputs))
    counts = 0
    for group in inputs:
        counts += len(set(group))
    return counts


def part2(inputs: List[str]) -> int:
    counts = 0
    for group in inputs:
        lines = group.splitlines()
        s = set(lines[0])
        for i in lines[1:]:
            s &= set(i)
        counts += len(s)
    return counts


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.read().split("\n\n")
    print(part1(data))
    print(part2(data))
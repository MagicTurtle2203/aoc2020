from typing import Dict

PREAMBLE_SIZE = 25


def part1(data: Dict[int, int]) -> int:
    for i in range(PREAMBLE_SIZE, len(data)):
        visited = set()
        pool = [data[j] for j in range(i - PREAMBLE_SIZE, i)]

        for k in pool:
            complement = data[i] - k
            if complement in visited:
                break
            else:
                visited.add(k)
        else:
            return data[i]
    return -1


def part2(data: Dict[int, int], target: int) -> int:
    def get_sum(data: Dict[int, int], first: int, second: int) -> int:
        return sum(data[i] for i in range(first, second + 1))

    first = 0
    second = 1

    while (s := get_sum(data, first, second)) != target:
        if s < target:
            second += 1
        else:
            first += 1

    pool = [data[i] for i in range(first, second + 1)]
    return max(pool) + min(pool)


if __name__ == "__main__":
    data = {}
    with open("input.txt") as file:
        for idx, line in enumerate(file):
            data[idx] = int(line.strip())
    p1 = part1(data)
    print(p1)
    print(part2(data, p1))

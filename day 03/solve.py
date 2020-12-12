from typing import List


def part1(data: List[str]) -> int:
    bottom = len(data)
    start_x = 0
    start_y = 0
    count = 0
    while start_y < bottom:
        if data[start_y][start_x] == "#":
            count += 1
        start_y += 1
        start_x += 3
        if start_y >= bottom:
            break
        if start_x >= len(data[start_y]):
            start_x %= len(data[start_y])
    return count


def get_trees(data: List[str], slope_x: int, slope_y: int) -> int:
    bottom = len(data)
    x = 0
    y = 0
    count = 0
    while y < bottom:
        if data[y][x] == "#":
            count += 1
        y += slope_y
        x += slope_x
        if y >= bottom:
            break
        if x >= len(data[y]):
            x %= len(data[y])
    return count


# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.


def part2(data: List[str]) -> int:
    return (
        get_trees(data, 1, 1)
        * get_trees(data, 3, 1)
        * get_trees(data, 5, 1)
        * get_trees(data, 7, 1)
        * get_trees(data, 1, 2)
    )


if __name__ == "__main__":
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(line.strip())
    # print(part1(data))
    print(part2(data))
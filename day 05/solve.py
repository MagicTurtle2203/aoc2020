from typing import List


def row_helper(letters: str, low: int, high: int) -> int:
    if high - low == 1:
        return low if letters == "F" else high
    mid = low + (high - low) // 2
    if letters[0] == "F":
        return row_helper(letters[1:], low, mid)
    else:
        return row_helper(letters[1:], mid + 1, high)


def column_helper(letters: str, low: int, high: int) -> int:
    if high - low == 1:
        return low if letters == "L" else high
    mid = low + (high - low) // 2
    if letters[0] == "L":
        return column_helper(letters[1:], low, mid)
    else:
        return column_helper(letters[1:], mid + 1, high)


def part1(inputs: List[str]) -> int:
    max_id = 0
    for i in inputs:
        row = row_helper(i[:7], 0, 127)
        col = column_helper(i[7:], 0, 7)
        out = row * 8 + col
        if out > max_id:
            max_id = out
    return max_id


def part2(inputs: List[str]) -> int:
    id_list = sorted([row_helper(i[:7], 0, 127) * 8 + column_helper(i[7:], 0, 7) for i in inputs])
    for i in range(1, len(id_list)):
        if id_list[i] - id_list[i - 1] > 1:
            return id_list[i] - 1


# "BFFFBBFRRR"
# "1000110111"

if __name__ == "__main__":
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(line.strip())
    print(part1(data))
    print(part2(data))
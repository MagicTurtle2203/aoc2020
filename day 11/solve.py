import itertools
from typing import Dict, List, Optional, Union


def part1(data: List[List[str]]) -> int:
    # apply rules until it seats don't change anymore
    empty_counts = 0
    occupied_counts = 0

    for row in data:
        for col in row:
            if col == "L":
                empty_counts += 1
            elif col == "#":
                occupied_counts += 1

    while True:
        change_to_occupied = []
        change_to_empty = []

        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == "L":
                    change = True
                    for (i, j) in itertools.product([-1, 0, 1], repeat=2):
                        if i == 0 and j == 0:
                            continue

                        new_x = i + x
                        new_y = j + y

                        if 0 <= new_x < len(data[y]) and 0 <= new_y < len(data) and data[new_y][new_x] == "#":
                            change = False
                            break
                    if change:
                        change_to_occupied.append((x, y))
                elif data[y][x] == "#":
                    counts = 0
                    for (i, j) in itertools.product([-1, 0, 1], repeat=2):
                        if i == 0 and j == 0:
                            continue

                        new_x = i + x
                        new_y = j + y

                        if 0 <= new_x < len(data[y]) and 0 <= new_y < len(data) and data[new_y][new_x] == "#":
                            counts += 1

                    if counts >= 4:
                        change_to_empty.append((x, y))

        for (x, y) in change_to_occupied:
            data[y][x] = "#"
        for (x, y) in change_to_empty:
            data[y][x] = "L"

        new_occupied_count = 0
        new_empty_count = 0

        for row in data:
            for col in row:
                if col == "L":
                    new_empty_count += 1
                elif col == "#":
                    new_occupied_count += 1

        if new_empty_count == empty_counts and new_occupied_count == occupied_counts:
            break
        else:
            empty_counts = new_empty_count
            occupied_counts = new_occupied_count

    return occupied_counts


def part2(data: List[List[str]]) -> int:
    # apply rules until it seats don't change anymore
    empty_counts = 0
    occupied_counts = 0

    for row in data:
        for col in row:
            if col == "L":
                empty_counts += 1
            elif col == "#":
                occupied_counts += 1

    while True:
        change_to_occupied = []
        change_to_empty = []

        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == "L":
                    change = True

                    # look up
                    start_x = x
                    start_y = y - 1

                    while 0 <= start_y < len(data) and data[start_y][start_x] == ".":
                        start_y -= 1

                    if 0 <= start_y < len(data) and data[start_y][start_x] == "#":
                        change = False

                    # look down
                    start_x = x
                    start_y = y + 1

                    while 0 <= start_y < len(data) and data[start_y][start_x] == ".":
                        start_y += 1

                    if 0 <= start_y < len(data) and data[start_y][start_x] == "#":
                        change = False

                    # look left
                    start_x = x - 1
                    start_y = y

                    while 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == ".":
                        start_x -= 1

                    if 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        change = False

                    # look right
                    start_x = x + 1
                    start_y = y

                    while 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == ".":
                        start_x += 1

                    if 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        change = False

                    # look up-left
                    start_x = x - 1
                    start_y = y - 1

                    while (
                        0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "."
                    ):
                        start_x -= 1
                        start_y -= 1

                    if 0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        change = False

                    # look up-right
                    start_x = x + 1
                    start_y = y - 1

                    while (
                        0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "."
                    ):
                        start_x += 1
                        start_y -= 1

                    if 0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        change = False

                    # look down-left
                    start_x = x - 1
                    start_y = y + 1

                    while (
                        0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "."
                    ):
                        start_x -= 1
                        start_y += 1

                    if 0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        change = False

                    # look down-right
                    start_x = x + 1
                    start_y = y + 1

                    while (
                        0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "."
                    ):
                        start_x += 1
                        start_y += 1

                    if 0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        change = False

                    if change:
                        change_to_occupied.append((x, y))
                elif data[y][x] == "#":
                    counts = 0

                    # look up
                    start_x = x
                    start_y = y - 1

                    while 0 <= start_y < len(data) and data[start_y][start_x] == ".":
                        start_y -= 1

                    if 0 <= start_y < len(data) and data[start_y][start_x] == "#":
                        counts += 1

                    # look down
                    start_x = x
                    start_y = y + 1

                    while 0 <= start_y < len(data) and data[start_y][start_x] == ".":
                        start_y += 1

                    if 0 <= start_y < len(data) and data[start_y][start_x] == "#":
                        counts += 1

                    # look left
                    start_x = x - 1
                    start_y = y

                    while 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == ".":
                        start_x -= 1

                    if 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        counts += 1

                    # look right
                    start_x = x + 1
                    start_y = y

                    while 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == ".":
                        start_x += 1

                    if 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        counts += 1

                    # look up-left
                    start_x = x - 1
                    start_y = y - 1

                    while (
                        0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "."
                    ):
                        start_x -= 1
                        start_y -= 1

                    if 0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        counts += 1

                    # look up-right
                    start_x = x + 1
                    start_y = y - 1

                    while (
                        0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "."
                    ):
                        start_x += 1
                        start_y -= 1

                    if 0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        counts += 1

                    # look down-left
                    start_x = x - 1
                    start_y = y + 1

                    while (
                        0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "."
                    ):
                        start_x -= 1
                        start_y += 1

                    if 0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        counts += 1

                    # look down-right
                    start_x = x + 1
                    start_y = y + 1

                    while (
                        0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "."
                    ):
                        start_x += 1
                        start_y += 1

                    if 0 <= start_y < len(data) and 0 <= start_x < len(data[start_y]) and data[start_y][start_x] == "#":
                        counts += 1

                    if counts >= 5:
                        change_to_empty.append((x, y))

        for (x, y) in change_to_occupied:
            data[y][x] = "#"
        for (x, y) in change_to_empty:
            data[y][x] = "L"

        new_occupied_count = 0
        new_empty_count = 0

        for row in data:
            for col in row:
                if col == "L":
                    new_empty_count += 1
                elif col == "#":
                    new_occupied_count += 1

        if new_empty_count == empty_counts and new_occupied_count == occupied_counts:
            break
        else:
            empty_counts = new_empty_count
            occupied_counts = new_occupied_count

    return occupied_counts


if __name__ == "__main__":
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(list(line.strip()))

    print(part1(data))
    print(part2(data))

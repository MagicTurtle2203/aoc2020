from typing import Dict, List, Optional, Tuple, Union
from collections import namedtuple
from itertools import product

coord_3d = namedtuple("coord_3d", "x y z")
coord_4d = namedtuple("coord_4d", "x y z w")


def check_neighbors_3d(c, d) -> int:
    count_active = 0
    for int_x, int_y, int_z in product((-1, 0, 1), repeat=3):
        if int_x == 0 and int_y == 0 and int_z == 0:
            continue
        new_x = int_x + c.x
        new_y = int_y + c.y
        new_z = int_z + c.z

        if (cd := coord_3d(new_x, new_y, new_z)) in d:
            if d[cd] == 1:
                count_active += 1
    if c in d and d[c] == 1:
        if count_active == 2 or count_active == 3:
            return 1
        else:
            return 0
    else:
        if count_active == 3:
            return 1
        else:
            return 0


def part1():
    data = list(
        map(
            list,
            """.###.#.#
####.#.#
#.....#.
####....
#...##.#
########
..#####.
######.#""".splitlines(),
        )
    )

    cubes = {}

    for y in range(len(data)):
        for x in range(len(data[y])):
            cubes[coord_3d(x, y, 0)] = 1 if data[y][x] == "#" else 0

    min_x = min_y = min_z = 0
    max_y = len(data)
    max_x = len(data[0])
    max_z = 1

    for _ in range(6):
        min_x -= 1
        min_y -= 1
        min_z -= 1
        max_x += 1
        max_y += 1
        max_z += 1

        temp = {}

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                for z in range(min_z, max_z):
                    c = coord_3d(x, y, z)
                    temp[c] = check_neighbors_3d(c, cubes)

        cubes.update(temp)

    return sum(i == 1 for i in cubes.values())


def check_neighbors_4d(c: coord_4d, d) -> int:
    count_active = 0
    for int_x, int_y, int_z, int_w in product((-1, 0, 1), repeat=4):
        if int_x == 0 and int_y == 0 and int_z == 0 and int_w == 0:
            continue
        new_x = int_x + c.x
        new_y = int_y + c.y
        new_z = int_z + c.z
        new_w = int_w + c.w

        if (cd := coord_4d(new_x, new_y, new_z, new_w)) in d:
            if d[cd] == 1:
                count_active += 1
    if c in d and d[c] == 1:
        if count_active == 2 or count_active == 3:
            return 1
        else:
            return 0
    else:
        if count_active == 3:
            return 1
        else:
            return 0


def part2():
    data = list(
        map(
            list,
            """.###.#.#
####.#.#
#.....#.
####....
#...##.#
########
..#####.
######.#""".splitlines(),
        )
    )

    cubes = {}

    for y in range(len(data)):
        for x in range(len(data[y])):
            cubes[coord_4d(x, y, 0, 0)] = 1 if data[y][x] == "#" else 0

    min_x = min_y = min_z = min_w = 0
    max_y = len(data)
    max_x = len(data[0])
    max_z = 1
    max_w = 1

    for _ in range(6):
        min_x -= 1
        min_y -= 1
        min_z -= 1
        min_w -= 1
        max_x += 1
        max_y += 1
        max_z += 1
        max_w += 1

        temp = {}

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                for z in range(min_z, max_z):
                    for w in range(min_w, max_w):
                        c = coord_4d(x, y, z, w)
                        temp[c] = check_neighbors_4d(c, cubes)

        cubes.update(temp)

    return sum(i == 1 for i in cubes.values())


if __name__ == "__main__":
    print(part1())
    print(part2())

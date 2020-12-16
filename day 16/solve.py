import re
from typing import Dict, List, Optional, Union


def part1(data: List[str]) -> int:
    field_re = re.compile(r"^[\w\s]+:\s(\d+)-(\d+)+\sor\s(\d+)-(\d+)$")
    index = 0

    min_n1, max_n2, min_n3, max_n4 = None, None, None, None

    while m := field_re.match(data[index]):
        n1, n2, n3, n4 = list(map(int, m.groups()))
        if min_n1 is None or n1 < min_n1:
            min_n1 = n1
        if max_n2 is None or n2 > max_n2:
            max_n2 = n2
        if min_n3 is None or n3 < min_n3:
            min_n3 = n3
        if max_n4 is None or n4 > max_n4:
            max_n4 = n4
        index += 1

    checker = lambda x: (min_n1 <= x <= max_n2) or (min_n3 <= x <= max_n4)

    invalid = []

    index += 5
    while index < len(data):
        numbers = map(int, data[index].split(","))
        for number in numbers:
            if not checker(number):
                invalid.append(number)
        index += 1

    return sum(invalid)


def part2(data: List[str]) -> int:
    field_re = re.compile(r"^([\w\s]+):\s(\d+)-(\d+)+\sor\s(\d+)-(\d+)$")
    index = 0

    fields = {}

    while m := field_re.match(data[index]):
        field_name, n1, n2, n3, n4 = m.groups()
        fields[field_name] = (lambda a, b, c, d: lambda x: (int(a) <= x <= int(b)) or (int(c) <= x <= int(d)))(
            n1, n2, n3, n4
        )
        index += 1

    index += 2
    my_ticket = list(map(int, data[index].split(",")))

    index += 3
    valid = set(range(index, len(data)))

    while index < len(data):
        numbers = map(int, data[index].split(","))
        for number in numbers:
            if not any(field(number) for field in fields.values()):
                valid.remove(index)
        index += 1

    field_locs = {name: list(range(len(my_ticket))) for name in fields}

    queue = list(fields.items())
    name, field = queue.pop(0)
    while len(queue) > 0:
        if len(field_locs[name]) == 1:
            for f in set(field_locs) - {name}:
                if field_locs[name][0] in field_locs[f]:
                    field_locs[f].remove(field_locs[name][0])
        else:
            for ticket in valid:
                for ticket in valid:
                    for idx, number in enumerate(map(int, data[ticket].split(","))):
                        if not field(number) and idx in field_locs[name]:
                            field_locs[name].remove(idx)
                if len(field_locs[name]) > 1:
                    queue.append((name, field))
                    break
                else:
                    for f in set(field_locs) - {name}:
                        if field_locs[name][0] in field_locs[f]:
                            field_locs[f].remove(field_locs[name][0])
                    break
        name, field = queue.pop(0)

    out = 1

    for name, loc in field_locs.items():
        if name.startswith("departure"):
            out *= my_ticket[loc[0]]

    return out


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.read().splitlines()
    print(part1(data))
    print(part2(data))

from typing import Dict, List, Optional, Union
import re
import itertools


def apply_mask(mask: str, val: int) -> int:
    out = ""

    for m, v in zip(mask, bin(val)[2:].rjust(36, "0")):
        if m == "X":
            out += v
        else:
            out += m

    return int(out, 2)


def part1(data: List[str]) -> int:
    d = {}
    mem_re = re.compile(r"mem\[(\d+)\]\s=\s(\d+)")
    mask_re = re.compile(r"mask = ([01X]+)")

    current_mask = ""

    for line in data:
        if s := mask_re.match(line):
            current_mask = s[1]
        elif s := mem_re.match(line):
            d[s[1]] = apply_mask(current_mask, int(s[2]))

    return sum(d.values())


def get_addresses(mask: str, address: int) -> List[int]:
    intermediate = ""
    x_count = mask.count("X")

    for m, v in zip(mask, bin(address)[2:].rjust(36, "0")):
        if m == "X":
            intermediate += "{}"
        elif m == "1":
            intermediate += m
        else:
            intermediate += v

    return [int(intermediate.format(*i), 2) for i in itertools.product((0, 1), repeat=x_count)]


def part2(data: List[str]) -> int:
    d = {}
    mem_re = re.compile(r"mem\[(\d+)\]\s=\s(\d+)")
    mask_re = re.compile(r"mask = ([01X]+)")

    current_mask = ""

    for line in data:
        if s := mask_re.match(line):
            current_mask = s[1]
        elif s := mem_re.match(line):
            for addr in get_addresses(current_mask, int(s[1])):
                d[addr] = int(s[2])

    return sum(d.values())


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.read().splitlines()
    # print(part1(data))
    print(part2(data))

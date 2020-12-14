from typing import Dict, List, MutableMapping, Optional, Union


def part1(target: int, buses: List[str]) -> float:
    earliest = float("inf")
    bus_id = None

    for bus in buses:
        if bus == "x":
            continue
        else:
            number = int(bus)
            next_arrival = target - (target % number) + number
            if next_arrival < earliest:
                earliest = next_arrival
                bus_id = number

    return bus_id * (earliest - target)


def part2(buses: List[str]) -> None:
    # Did by hand
    pass


if __name__ == "__main__":
    with open("input.txt") as file:
        target = int(file.readline().strip())
        buses = file.readline().strip().split(",")
    print(part1(target, buses))

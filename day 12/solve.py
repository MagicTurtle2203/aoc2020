from typing import Dict, List, Optional, Union


class Boat:
    def __init__(self) -> None:
        self.direction = 0  # E: 0, S: 1, W: 2, N: 3
        self.x = 0
        self.y = 0

    def forward(self, n: int) -> None:
        if self.direction == 0:
            self.x += n
        elif self.direction == 1:
            self.y -= n
        elif self.direction == 2:
            self.x -= n
        else:
            self.y += n

    def north(self, n: int) -> None:
        self.y += n

    def south(self, n: int) -> None:
        self.y -= n

    def east(self, n: int) -> None:
        self.x += n

    def west(self, n: int) -> None:
        self.x -= n

    def left(self, degrees: int) -> None:
        degrees //= 90
        self.direction = (self.direction - degrees) % 4

    def right(self, degrees: int) -> None:
        degrees //= 90
        self.direction = (self.direction + degrees) % 4


class Waypoint(Boat):
    def __init__(self, boat: Boat) -> None:
        super().__init__()
        self.x = 10
        self.y = 1
        self.boat = boat

    def forward(self, n: int) -> None:
        relative_x = self.x - self.boat.x
        relative_y = self.y - self.boat.y

        self.boat.x += relative_x * n
        self.boat.y += relative_y * n

        self.x = self.boat.x + relative_x
        self.y = self.boat.y + relative_y

    def left(self, degrees: int) -> None:
        relative_x = self.x - self.boat.x
        relative_y = self.y - self.boat.y

        times = degrees // 90

        for _ in range(times):
            relative_x, relative_y = relative_y, relative_x
            relative_x *= -1

        self.x = self.boat.x + relative_x
        self.y = self.boat.y + relative_y

    def right(self, degrees: int) -> None:
        relative_x = self.x - self.boat.x
        relative_y = self.y - self.boat.y

        times = degrees // 90

        for _ in range(times):
            relative_x, relative_y = relative_y, relative_x
            relative_y *= -1

        self.x = self.boat.x + relative_x
        self.y = self.boat.y + relative_y


def part1(data: List[str]) -> int:
    boat = Boat()
    for instruction in data:
        cmd, val = instruction[:1], int(instruction[1:])
        if cmd == "N":
            boat.north(val)
        elif cmd == "S":
            boat.south(val)
        elif cmd == "E":
            boat.east(val)
        elif cmd == "W":
            boat.west(val)
        elif cmd == "L":
            boat.left(val)
        elif cmd == "R":
            boat.right(val)
        else:
            boat.forward(val)
    return abs(boat.x) + abs(boat.y)


def part2(data: List[str]) -> int:
    boat = Boat()
    waypoint = Waypoint(boat)
    for instruction in data:
        cmd, val = instruction[:1], int(instruction[1:])
        if cmd == "N":
            waypoint.north(val)
        elif cmd == "S":
            waypoint.south(val)
        elif cmd == "E":
            waypoint.east(val)
        elif cmd == "W":
            waypoint.west(val)
        elif cmd == "L":
            waypoint.left(val)
        elif cmd == "R":
            waypoint.right(val)
        else:
            waypoint.forward(val)
    return abs(boat.x) + abs(boat.y)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.read().splitlines()
    print(part1(data))
    print(part2(data))

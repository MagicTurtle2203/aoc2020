import sys
from pathlib import Path

TEMPLATE = """from typing import Dict, List, Optional, Union


def part1():
    pass


def part2():
    pass


if __name__ == "__main__":
    with open("input1.txt") as file:
        pass
    print(part1())
    print(part2())
"""

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        raise Exception("You must provide the day")

    path = Path(__file__).parent

    if (path / f"day {args[1]}").exists():
        raise Exception("That day already exists")
    else:
        (path / f"day {args[1]}").mkdir()

    new_file = path / f"day {args[1]}" / "solve.py"
    new_file.touch()

    with open(new_file, "w") as file:
        file.write(TEMPLATE)

    print("done.")

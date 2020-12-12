from typing import Dict, Optional


class Instruction:
    def __init__(self, type: str, value: int) -> None:
        self.type = type
        self.value = value


def part1(instructions: Dict[int, Instruction]) -> int:
    acc = 0

    index = 0
    visited = set()

    while True:
        if index in visited:
            return acc
        else:
            visited.add(index)
        inst = instructions[index]
        if inst.type == "acc":
            acc += inst.value
            index += 1
        elif inst.type == "jmp":
            index += inst.value
        else:
            index += 1


def helper(instructions: Dict[int, Instruction]) -> Optional[int]:
    acc = 0

    index = 0
    visited = set()

    max_index = max(instructions)

    while True:
        if index in visited:
            return None
        elif index >= max_index:
            return acc
        else:
            visited.add(index)
        inst = instructions[index]
        if inst.type == "acc":
            acc += inst.value
            index += 1
        elif inst.type == "jmp":
            index += inst.value
        else:
            index += 1


def part2(instructions: Dict[int, Instruction]) -> int:
    for idx, instruction in instructions.items():
        if instruction.type == "jmp":
            instructions_copy = instructions.copy()
            instructions_copy[idx] = Instruction("nop", instructions[idx].value)
            res = helper(instructions_copy)
            if res is not None:
                return res
        elif instruction.type == "nop":
            instructions_copy = instructions.copy()
            instructions_copy[idx] = Instruction("jmp", instructions[idx].value)
            res = helper(instructions_copy)
            if res is not None:
                return res


if __name__ == "__main__":
    instructions = {}
    with open("input.txt") as file:
        for idx, line in enumerate(file):
            instructions[idx] = (lambda x: Instruction(x[0], int(x[1])))(line.strip().split())
    print(part1(instructions))
    print(part2(instructions))
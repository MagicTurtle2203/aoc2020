from typing import Dict, List, Optional, Union
import re
from collections import deque


def sya_part1(data: str) -> List[Union[str, int]]:
    r = re.compile(r"\d+|[\(\)+*]")
    output = []
    op_stack = []

    for i in r.findall(data):
        if i.isdigit():
            output.append(int(i))
        elif i == "*":
            if len(op_stack) > 0 and (op_stack[-1] == "*" or op_stack[-1] == "+"):
                output.append(op_stack.pop())
                op_stack.append(i)
            else:
                op_stack.append(i)
        elif i == "+":
            if len(op_stack) > 0 and (op_stack[-1] == "*" or op_stack[-1] == "+"):
                output.append(op_stack.pop())
                op_stack.append(i)
            else:
                op_stack.append(i)
        elif i == "(":
            op_stack.append(i)
        elif i == ")":
            while op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()

    while len(op_stack) > 0:
        output.append(op_stack.pop())

    return output


def evaluate(data: List[Union[str, int]]) -> int:
    data = deque(data)
    num_stack = []

    while len(data) > 0:
        while data[0] not in ("+", "*"):
            num_stack.append(data.popleft())

        operator = data.popleft()
        num1 = num_stack.pop()
        num2 = num_stack.pop()

        if operator == "+":
            num_stack.append(num1 + num2)
        elif operator == "*":
            num_stack.append(num1 * num2)

    return num_stack[0]


def part1(data: List[str]) -> int:
    return sum(evaluate(sya_part1(i)) for i in data)


def sya_part2(data: List[str]) -> List[Union[str, int]]:
    r = re.compile(r"\d+|[\(\)+*]")
    output = []
    op_stack = []

    for i in r.findall(data):
        if i.isdigit():
            output.append(int(i))
        elif i == "*":
            if len(op_stack) > 0 and (op_stack[-1] == "*" or op_stack[-1] == "+"):
                output.append(op_stack.pop())
                op_stack.append(i)
            else:
                op_stack.append(i)
        elif i == "+":
            if len(op_stack) > 0 and op_stack[-1] == "+":
                output.append(op_stack.pop())
                op_stack.append(i)
            else:
                op_stack.append(i)
        elif i == "(":
            op_stack.append(i)
        elif i == ")":
            while op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()

    while len(op_stack) > 0:
        output.append(op_stack.pop())

    return output


def part2(data: List[str]) -> int:
    return sum(evaluate(sya_part2(i)) for i in data)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.read().splitlines()
    print(part1(data))
    print(part2(data))

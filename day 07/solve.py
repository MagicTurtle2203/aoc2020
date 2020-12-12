import re
from typing import Dict, List


def helper(bag: str, bag_dict: Dict[str, List[str]]) -> int:
    # return 1 if leads to shiny gold bag else 0
    if len(bag_dict[bag]) == 0:
        return 0
    elif "shiny gold bags" in bag_dict[bag]:
        return 1
    else:
        counts = 0
        for b in bag_dict[bag]:
            counts += helper(b, bag_dict)
        if counts > 0:
            return 1
        else:
            return 0


def part1(data: List[str]) -> int:
    line_re = re.compile(r"^([\w\s]+)\scontain\s([\w\s,]+).$")
    bag_re = re.compile(r"\d\s([a-zA-Z\s]+)")

    bag_dict = {}
    for line in data:
        start_bag, end_bags = line_re.match(line.strip()).groups()
        bag_dict[start_bag] = list(map(lambda x: x if x[-1] == "s" else x + "s", bag_re.findall(end_bags)))

    count = 0
    for start_bag, values in bag_dict.items():
        if "shiny gold bags" in values:
            count += 1
        else:
            for bag in values:
                res = helper(bag, bag_dict)
                if res == 1:
                    count += 1
                    break
    return count


def helper2(bag: str, bag_dict: Dict[str, List[str]]) -> int:
    if len(bag_dict[bag]) == 0:
        return 1
    else:
        return sum(helper2(b, bag_dict) for b in bag_dict[bag]) + 1


def part2(data: List[str]) -> int:
    line_re = re.compile(r"^([\w\s]+)\scontain\s([\w\s,]+).$")
    bag_re = re.compile(r"(\d)\s([a-zA-Z\s]+)")

    bag_dict = {}
    for line in data:
        start_bag, end_bags = line_re.match(line.strip()).groups()
        bag_dict[start_bag] = []
        for num, bag in bag_re.findall(end_bags):
            bag_dict[start_bag] += [(bag if bag[-1] == "s" else bag + "s") for _ in range(int(num))]

    return helper2("shiny gold bags", bag_dict) - 1


if __name__ == "__main__":
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append(line.strip())
    print(part1(data))
    print(part2(data))

import re
from typing import List


def part1(inputs: List[str]) -> int:
    r = re.compile(r"(\w+):#?\w+")
    count = 0
    for line in inputs:
        match = r.findall(line)
        if (
            "byr" in match
            and "iyr" in match
            and "eyr" in match
            and "hgt" in match
            and "hcl" in match
            and "ecl" in match
            and "pid" in match
        ):
            count += 1
    return count


def part2(inputs: List[str]) -> int:
    r = re.compile(r"(\w+):(#?\w+)")
    count = 0
    for line in inputs:
        match = r.findall(line)
        d = {key: value for key, value in match}
        if "byr" in d and "iyr" in d and "eyr" in d and "hgt" in d and "hcl" in d and "ecl" in d and "pid" in d:
            count += (
                (1920 <= int(d["byr"]) <= 2002)
                and (2010 <= int(d["iyr"]) <= 2020)
                and (2020 <= int(d["eyr"]) <= 2030)
                and (
                    (d["hgt"][-2:] == "cm" and 150 <= int(d["hgt"][:-2]) <= 193)
                    or (d["hgt"][-2:] == "in" and 59 <= int(d["hgt"][:-2]) <= 76)
                )
                and re.match(r"^#[0-9a-f]{6}$", d["hcl"]) is not None
                and d["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
                and re.match(r"^\d{9}$", d["pid"]) is not None
            )
    return count


if __name__ == "__main__":
    long_string = ""
    with open("input.txt") as file:
        for line in file:
            if line == "\n":
                long_string += "|"
            else:
                long_string += line.replace("\n", " ")
    inputs = long_string.split("|")
    print(part1(inputs))
    print(part2(inputs))

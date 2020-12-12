# def parse_line(line: str) -> bool:
import re

r = re.compile(r"(\d+)-(\d+)\s+(\w):\s+(\w+)")
counts = 0
with open("input.txt") as f:
    for line in f:
        min_, max_, char, string = r.match(line.strip()).groups()
        counts += int(min_) <= string.count(char) <= int(max_)
print(counts)
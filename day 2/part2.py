import re

r = re.compile(r"(\d+)-(\d+)\s+(\w):\s+(\w+)")
counts = 0
with open("input.txt") as f:
    for line in f:
        pos1, pos2, char, string = r.match(line.strip()).groups()
        pos1, pos2 = int(pos1), int(pos2)
        counts += (string[pos1 - 1] == char) ^ (string[pos2 - 1] == char)
print(counts)
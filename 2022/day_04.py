from pathlib import Path

ranges = Path("inputs/day_04.txt").read_text().strip().split("\n")

def parse(line):
    return tuple(map(lambda i: tuple(map(int, i.split("-"))), line.split(",")))

def fully_overlaps(ranges):
    if ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]:
        return True

    if ranges[1][0] <= ranges[0][0] and ranges[1][1] >= ranges[0][1]:
        return True

    return False

print(len(tuple(filter(fully_overlaps, tuple(map(parse, ranges))))))

def overlaps(ranges):
    if ranges[0][0] <= ranges[1][0] and ranges[1][0] <= ranges[0][1]:
        return True

    if ranges[1][0] <= ranges[0][0] and ranges[0][0] <= ranges[1][1]:
        return True

    return False

print(len(tuple(filter(overlaps, tuple(map(parse, ranges))))))

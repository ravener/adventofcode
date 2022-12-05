from pathlib import Path

contents = Path("inputs/day_03.txt").read_text().strip().split("\n")

def priority(item):
    return ord(item) - (96 if item.islower() else 38)

def split_compartments(items):
    size = len(items) // 2
    return (items[:size], items[size:])

def find_duplicate(compartments):
    for items in compartments[0]:
        for item in items:
            if item in compartments[1]:
                return item

print(sum(map(priority, map(find_duplicate, map(split_compartments, contents)))))

groups = [contents[i:i+3] for i in range(0, len(contents), 3)]

def find_common(group):
    for items in group[0]:
        for item in items:
            if item in group[1] and item in group[2]:
                return item

print(sum(map(priority, map(find_common, groups))))

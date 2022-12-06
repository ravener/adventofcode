from pathlib import Path

stream = Path("inputs/day_06.txt").read_text().strip()

def part_one():
    for i, v in enumerate(stream):
        if len(set(stream[i:i+4])) == 4:
            return i+4

def part_two():
    for i, v in enumerate(stream):
        if len(set(stream[i:i+14])) == 14:
            return i+14

print(part_one())
print(part_two())

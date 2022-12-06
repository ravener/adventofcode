from pathlib import Path
from copy import deepcopy

(crates, moves) = Path("inputs/day_05.txt").read_text().strip().split("\n\n")

stacks = []
crates = crates.split("\n")[:-1]
crates.reverse()

for stack in crates:
    for i, crate in enumerate(stack[1::4]):
        if crate == " ":
            continue

        if i >= len(stacks):
            stacks.append([])

        stacks[i].append(crate)

def part_one(stacks):
    for move in moves.split("\n"):
        (_, count, _, location, _, destination) = move.split(" ")
        count = int(count)
        location = int(location)-1
        destination = int(destination)-1

        for i in range(count):
            stacks[destination].append(stacks[location].pop())

    return "".join([stack[-1] for stack in stacks])

def part_two(stacks):
    for move in moves.split("\n"):
        (_, count, _, location, _, destination) = move.split(" ")
        count = int(count)
        location = int(location)-1
        destination = int(destination)-1
        stacks[destination].extend(reversed([stacks[location].pop() for i in range(count)]))

    return "".join([stack[-1] for stack in stacks])

print(part_one(deepcopy(stacks)))
print(part_two(deepcopy(stacks)))

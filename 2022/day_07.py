from pathlib import Path
from collections import defaultdict

commands = Path("inputs/day_07.txt").read_text().strip().split("\n")
cwd = []
dirs = defaultdict(int)

for command in commands:
    parts = command.split(" ")
    
    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "..":
                cwd.pop()
            elif parts[2]:
                cwd.append(parts[2])
    elif parts[0] != "dir":
        for i in range(len(cwd)):
            dirs[tuple(cwd[:i+1])] += int(parts[0])

print(sum(i for i in dirs.values() if i <= 100000))
print(min(i for i in dirs.values() if i >= dirs[("/",)] - 40000000))

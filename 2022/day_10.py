from pathlib import Path

instructions = Path("inputs/day_10.txt").read_text().splitlines()

X = 1
cycles = 0
ip = 0
in_add = False
signals = []
crt = [[] for i in range(6)]
cur_row = 0

while True:
    cycles += 1

    if cycles in [20, 60, 100, 140, 180, 220]:
        signals.append(cycles * X)


    if ip >= len(instructions):
        break

    row = crt[cur_row]
    position = len(row)
    row.append("#" if position >= X-1 and position < X+2 else ".")
    if position == 39:
        cur_row += 1

    instruction = instructions[ip].split(" ")
    
    if instruction[0] == "noop":
        ip += 1
    elif instruction[0] == "addx":
        if in_add:
            ip += 1
            X += int(instruction[1])
            in_add = False
        else:
            in_add = True

print(sum(signals))
print("\n".join(map(lambda i: "".join(i), crt)))

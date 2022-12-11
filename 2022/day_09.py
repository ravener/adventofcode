from pathlib import Path

moves = Path("inputs/day_09.txt").read_text().splitlines()

def sign(n):
    if n == 0:
        return 0

    return 1 if n > 0 else -1

def simulate(n):
    positions = [[0, 0] for i in range(n)]
    visited = set()

    for move in moves:
        direction, count = move.split(" ")
    
        for i in range(int(count)):
            if direction == "L":
                positions[0][0] -= 1
            elif direction == "R":
                positions[0][0] += 1
            elif direction == "U":
                positions[0][1] += 1
            elif direction == "D":
                positions[0][1] -= 1

            for i in range(1, len(positions)):
                dx = positions[i - 1][0] - positions[i][0]
                dy = positions[i - 1][1] - positions[i][1]
    
                if abs(dx) >= 2 or abs(dy) >= 2:
                    positions[i][0] += sign(dx)
                    positions[i][1] += sign(dy)
            visited.add(tuple(positions[-1]))

    return len(visited)

print(simulate(2))
print(simulate(10))

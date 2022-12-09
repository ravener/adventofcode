from pathlib import Path

forest = Path("inputs/day_08.txt").read_text()
grid = [[int(i) for i in line] for line in forest.splitlines()]

# Given a tree, return all other trees on the way to the edge.
# From all directions.
def get_directions(i, j):
    west = list(reversed(grid[i][:j]))
    east = grid[i][j+1:]
    north = list(reversed([row[j] for row in grid[:i]]))
    south = [row[j] for row in grid[i+1:]]

    return [west, east, north, south]

def calculate_score(tree, directions):
    scores = []

    for direction in directions:
        view = 0
        for tile in direction:
            view += 1
            if tile >= tree:
                break

        scores.append(view)

    return scores[0] * scores[1] * scores[2] * scores[3]


# Count the trees that are always visible on the edge.
visible = len(grid)*2 + len(grid[0])*2 - 4
scores = []

# Figure out the rest of the trees, excluding the edges.
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        tree = grid[i][j]
        directions = get_directions(i, j)

        if any(all(tree > v for v in dt) for dt in directions):
            visible += 1

        scores.append(calculate_score(tree, directions))


print(visible)
print(max(scores))

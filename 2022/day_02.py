from pathlib import Path

guide = Path("inputs/day_02.txt").read_text().strip().split("\n")

ROCK = 1
PAPER = 2
SCISSORS = 3
DRAW = 3
WIN = 6

def calculate_score(line):
    opponent, play = line.split(" ")
    score = ord(play) - 87
    op = ord(opponent) - 64
    
    if score == op:
        return score + DRAW
    if op == ROCK and score == PAPER:
        return score + WIN
    elif op == ROCK and score == SCISSORS:
        return score
    elif op == PAPER and score == ROCK:
        return score
    elif op == PAPER and score == SCISSORS:
        return score + WIN
    elif op == SCISSORS and score == ROCK:
        return score + WIN
    elif op == SCISSORS and score == PAPER:
        return score

print(sum(map(calculate_score, guide)))

def calculate_results(line):
    opponent, results = line.split(" ")
    
    if results == "X":
        if opponent == "A":
            return SCISSORS
        elif opponent == "B":
            return ROCK
        elif opponent == "C":
            return PAPER
    elif results == "Y":
        return ord(opponent) - 64 + DRAW
    elif results == "Z":
        if opponent == "A":
            return PAPER + WIN
        elif opponent == "B":
            return SCISSORS + WIN
        elif opponent == "C":
            return ROCK + WIN

print(sum(map(calculate_results, guide)))

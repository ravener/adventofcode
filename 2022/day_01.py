from pathlib import Path

calories = Path("inputs/day_01.txt").read_text().strip().split("\n\n")
totals = sorted(map(lambda i: sum(map(int, i.split("\n"))), calories), reverse=True)

print(totals[0])
print(sum(totals[:3]))

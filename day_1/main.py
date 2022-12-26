
with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

data = raw_data[0]

solution_1 = None
solution_2 = None

floor = 0

for i, c in enumerate(data):
    if c == '(':
        floor += 1
    else:
        floor -= 1

    if floor == -1 and solution_2 is None:
        solution_2 = i + 1

solution_1 = floor

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

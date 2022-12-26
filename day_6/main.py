

with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

data = []

for line in raw_data:
    line = line.split()
    
    match line[0]:
        case "toggle":
            action = 2

        case "turn":
            match line[1]:
                case "on":
                    action = 1
                case "off":
                    action = 0

    x1, y1 = [int(i) for i in line[-3].split(',')]
    x2, y2 = [int(i) for i in line[-1].split(',')]

    data.append([action, (x1, y1), (x2, y2)])

# ------------------------------------------------- part 1 ------------------------------------------------- #

grid = [[0 for _ in range(1000)] for _ in range(1000)]

solution_1 = 0

for line in data:
    a, (r1, c1), (r2, c2) = line

    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            match a:
                case 0:
                    grid[r][c] = 0
                case 1:
                    grid[r][c] = 1
                case 2:
                    grid[r][c] = int(not grid[r][c])

for row in grid:
    solution_1 += sum(row)

# ------------------------------------------------- part 2 ------------------------------------------------- #

grid = [[0 for _ in range(1000)] for _ in range(1000)]

solution_2 = 0

for line in data:
    a, (r1, c1), (r2, c2) = line

    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            match a:

                # turn off
                case 0:
                    grid[r][c] = max(0, grid[r][c] - 1)

                # turn on
                case 1:
                    grid[r][c] += 1 
                
                # toggle
                case 2:
                    grid[r][c] += 2

for row in grid:
    solution_2 += sum(row)

# ---------------------------------------------------------------------------------------------------------- #

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# ---------------------------------------------------------------------------------------------------------- #

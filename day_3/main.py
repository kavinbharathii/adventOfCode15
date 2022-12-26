
with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

dirs = raw_data[0]

def solve(dirs, part_2 = False):
    santa = [0, 0]
    robo_santa = [0, 0]
    houses = set()
    for index, dir in enumerate(dirs):
        if part_2:
            match dir:
                case '^':
                    if index % 2: santa[0] -= 1
                    else: robo_santa[0] -= 1
                case 'v':
                    if index % 2: santa[0] += 1
                    else: robo_santa[0] += 1
                case '>':
                    if index % 2: santa[1] += 1
                    else: robo_santa[1] += 1
                case '<':        
                    if index % 2: santa[1] -= 1
                    else: robo_santa[1] -= 1

            houses.add(tuple(santa))
            houses.add(tuple(robo_santa))

        else:
            match dir:
                case '^':
                    santa[0] -= 1
                case 'v':
                    santa[0] += 1
                case '>':
                    santa[1] += 1
                case '<':        
                    santa[1] -= 1

            houses.add(tuple(santa))

    return len(houses)

# solution_1 = solve(dirs)
solution_2 = solve(dirs, True)

# print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

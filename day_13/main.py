
from itertools import permutations

with open("data.aoc", "r") as file:
    data = [line.strip('.\n') for line in file.readlines()]
    file.close()

happy = {}
name_code = {}
name_count = 0

for line in data:
    line = line.split()
    from_, to_ = line[0], line[-1]
    
    if from_ not in name_code:
        name_code[from_] = name_count
        name_count += 1

    if to_ not in name_code:
        name_code[to_] = name_count
        name_count += 1

    from_ = name_code[from_]
    to_ = name_code[to_]

    sign, value = line[2], line[3]
    
    if sign == "gain":
        sign = 1
    else:
        sign = -1

    happy[(from_, to_)] = sign * int(value)

# Part 1
maximum_happiness = 0

src = 0
all_perms = permutations(list(range(1, name_count)))

for perm in all_perms:
    prev = src
    perm_happiness = 0

    for vertex in perm:
        perm_happiness += happy[(prev, vertex)]
        perm_happiness += happy[(vertex, prev)]
        prev = vertex

    perm_happiness += happy[(prev, src)]
    perm_happiness += happy[(src, prev)]
    maximum_happiness = max(maximum_happiness, perm_happiness)

solution_1 = maximum_happiness

# Part 2
for i in name_code.values():
    happy[(name_count, i)] = 0
    happy[(i, name_count)] = 0

maximum_happiness = 0

src = 0
all_perms = permutations(list(range(1, name_count + 1)))

for perm in all_perms:
    prev = src
    perm_happiness = 0

    for vertex in perm:
        perm_happiness += happy[(prev, vertex)]
        perm_happiness += happy[(vertex, prev)]
        prev = vertex

    perm_happiness += happy[(prev, src)]
    perm_happiness += happy[(src, prev)]
    maximum_happiness = max(maximum_happiness, perm_happiness)

solution_2 = maximum_happiness

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")
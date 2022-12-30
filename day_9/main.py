from itertools import permutations

def get_data():
    with open("data.txt", "r") as file:
        raw_data = [line.strip() for line in file.readlines()]
        file.close()

    return raw_data

raw_data = get_data()
data = []
places = {}
counter = 0

for line in raw_data:
    line = line.split()
    from_ = line[0]
    to_ = line[2]
    weight = int(line[-1])

    if from_ not in places.keys():
        places[from_] = counter
        counter += 1

    if to_ not in places.keys():
        places[to_] = counter
        counter += 1

    data.append((places[from_], places[to_], weight))

def dist(from_, to_):
    for f, t, w in data:
        if from_ == f and to_ == t:
            return w

        elif from_ == t and to_ == f:
            return w

    return 0

def solve():
    vertices = [i for i in places.values()]
    all_possible_combinations = permutations(vertices)
    minimum_distance = 10e6
    maximum_distance = -10e6

    for possibility in all_possible_combinations:

        current = possibility[0]
        possible_distance = 0

        for next_ in possibility[1:]:
            possible_distance += dist(current, next_)
            current = next_

        minimum_distance = min(minimum_distance, possible_distance)
        maximum_distance = max(maximum_distance, possible_distance)

    return minimum_distance, maximum_distance       

solution_1, solution_2 = solve()
print(f"Part solution_1: {solution_1}")
print(f"Part solution_2: {solution_2}")
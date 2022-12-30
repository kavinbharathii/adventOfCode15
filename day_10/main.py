
data = "1113122113"
conways_constant = 1.303577269

def lookandsay(num):
    pointer = num[0]
    counter = 1
    res = ''

    for i in num[1:]:
        if i == pointer:
            counter += 1
        else:
            res += f"{counter}{pointer}"
            pointer = i
            counter = 1

    res += f"{counter}{pointer}"

    return res

# Iterate "40" times for part 1
for _ in range(40):
    data = lookandsay(data)

solution_1 = len(data)

# Iterate "50" times for part 2
for _ in range(10):
    data = lookandsay(data)

solution_2 = len(data)

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")
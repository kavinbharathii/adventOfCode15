
with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

def area(l, w, h):
    slack = min(l*w, w*h, l*h)
    total = 2 * (l*w + w*h + l*h)
    return slack + total

def ribbon(l, w, h):
    a, b = sorted([l, w, h])[:-1]
    wrap = 2 * a + 2 * b 
    bow = l * w * h
    return wrap + bow


solution_1 = 0
solution_2 = 0

for data in raw_data:
    l, w, h = [int(i) for i in data.split('x')]
    solution_1 += area(l, w, h)
    solution_2 += ribbon(l, w, h)

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")
    
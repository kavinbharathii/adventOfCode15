

with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()
    
vowels = 'aeiou'

def old_noice(data):
    vowel_count = sum([1 if char in vowels else 0 for char in data])
    if vowel_count < 3: return False

    consecutive_letter = False
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            consecutive_letter = True
            break

    if not consecutive_letter: return False

    forbidden = ['ab', 'cd', 'pq', 'xy']
    for s in forbidden:
        if s in data:
            return False

    return True

def new_noice(data):
    double_pairs = False
    for i in range(len(data) - 1):
        pair = data[i] + data[i + 1]
        if data.count(pair) >= 2:
            double_pairs = True
            break

    if not double_pairs: return False

    for i in range(len(data) - 2):
        if data[i] == data[i + 2]:
            return True

    return False


solution_1 = 0
solution_2 = 0


for data in raw_data:
    if old_noice(data): solution_1 += 1
    if new_noice(data): solution_2 += 1

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

data = "cqjxjnds"
alphas = "abcdefghjkmnpqrstuvwxyz"

def is_valid(pwd):

    # i, o, l shouldn't be in the password
    forbidden = 'iol'
    for letter in forbidden:
        if letter in pwd:
            return False

    # increasing consecutive three letters
    condition_1 = False
    for i in range(len(pwd) - 2):
        a, b, c = pwd[i], pwd[i + 1], pwd[i + 2]
        if (alphas.index(b) - alphas.index(a)) == 1 and (alphas.index(c) - alphas.index(b)) == 1:
            condition_1 = True
            break

    if not condition_1: return False

    # Non overlapping pairs
    total_pairs = 0
    last_pair_ind = 1
    for i in range(len(pwd) - 1):
        a, b = pwd[i], pwd[i + 1]
        if a == b:
            if i == last_pair_ind:
                continue
            else:
                total_pairs += 1
                last_pair_ind = i + 1

    if total_pairs < 2: return False

    return True

def next_password(pwd):
    if pwd == '':
        return ''
    elif pwd[-1] == 'z':
        return next_password(pwd[:-1]) + 'a'
    else:
        return pwd[:-1] + alphas[alphas.index(pwd[-1]) + 1]


while not is_valid(data):
    data = next_password(data)

print(f"Part 1: {data}")

data = next_password(data)

while not is_valid(data):
    data = next_password(data)

print(f"Part 2: {data}")

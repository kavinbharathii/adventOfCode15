

# ---------------------------------------------------- data/constants/functions ---------------------------------------------------- #

def get_data():
    with open("data.txt", "r") as file:
        raw_data = [line.strip() for line in file.readlines()]
        file.close()

    return raw_data

AND = ' AND '
OR = ' OR '
LSHIFT = ' LSHIFT '
RSHIFT = ' RSHIFT '
NOT = 'NOT'

def nott(x):
    x = str(bin(x))[2:].zfill(16)
    y = ''.join(['1' if i == '0' else '0' for i in x])
    return int(y, 2)

# ------------------------------------------------------------ part 1 ------------------------------------------------------------ # 

data = {}
raw_data = get_data()

for line in raw_data:
    signal, wire = line.split(' -> ')
    data[wire] = signal


def solve(wire):    
    if wire.isnumeric():
        return int(wire)

    signal = data[wire]

    if type(signal) == int or signal.isnumeric():
        data[wire] = int(signal)

    else:
        if AND in signal:
            a, b = signal.split(AND)
            data[wire] = solve(a) & solve(b)

        elif OR in signal:
            a, b = signal.split(OR)
            data[wire] = solve(a) | solve(b)

        elif LSHIFT in signal:
            a, b = signal.split(LSHIFT)
            data[wire] = solve(a) << int(b)

        elif RSHIFT in signal:
            a, b = signal.split(RSHIFT)
            data[wire] = solve(a) >> int(b)

        elif NOT in signal:
            _, a = signal.split()
            data[wire] = nott(solve(a))
        
        else:
            data[wire] = solve(signal)

    return data[wire]

solution_1 = solve('a')

# ------------------------------------------------------------ part 2 ------------------------------------------------------------ # 

data = {}
raw_data = get_data()

for line in raw_data:
    signal, wire = line.split(' -> ')
    data[wire] = signal

data['b'] = solution_1
solution_2 = solve('a')

# -------------------------------------------------------------------------------------------------------------------------------- # 

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# -------------------------------------------------------------------------------------------------------------------------------- # 

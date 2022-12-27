

def get_data():
    with open("data.txt", "r") as file:
        raw_data = [line.strip() for line in file.readlines()]
        file.close()

    return raw_data

raw_data = get_data()

code_total = 0
mem_total = 0
encode_total = 0

for line in raw_data:
    code_total += len(line)
    new_line = eval(line)
    mem_total += len(new_line)

    encode_line = '"' + line.replace('\\', '\\\\').replace('\"', '\\\"').replace('"', '\"') + '"'
    encode_total += len(encode_line)

solution_1 = code_total - mem_total
solution_2 = encode_total - code_total


print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")



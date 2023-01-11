
import json

with open("data.aoc", "r") as file:
    data = file.readline()
    file.close()

nums = []

def get_total(data):
    curr = ''
    for i in data:
        if i in "-1234567890":
            curr += i
        else:
            if len(curr) > 0:
                nums.append(int(curr))
            curr = ''

    return sum(nums)

solution_1 = get_total(data)
print(solution_1)

json_data = json.loads(data)

import re
import json

def sum_nums(inp):
    nums = [int(x) for x in re.findall(r'-?\d+', str(inp))]
    return sum(nums)

def sum_red(inp):
    if type(inp) in (int, str):
        return 0
    if type(inp) == list:
        return sum(sum_red(x) for x in inp)
    if type(inp) == dict:
        if 'red' in inp.values():
            return sum_nums(inp)
        return sum_red(list(inp.values()))

total_sum = sum_nums(json_data)
red_sum = sum_red(json_data)
print(total_sum - red_sum)


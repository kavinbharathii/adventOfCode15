from hashlib import md5

key = "pqrstuv"

solution_1 = 1048970

def is_valid(num):
    hash = key + str(num)
    hash = hash.encode()
    hash = md5(hash)
    print(hash)
    hash = str(hash).split()[-1].split('x')[-1]
    print(hash)
    print(hash[:5] == "00000")
    return hash[:5] == "00000"

while not is_valid(solution_1):
    solution_1 += 1

print(solution_1)

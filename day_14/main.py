
import re
from reindeer import Reindeer

with open("data.aoc", "r") as file:
    data = [line.strip('.\n') for line in file.readlines()]
    file.close()

reins = {}

for line in data:
    deer = line.split()[0]
    nums = (re.findall('[0-9]+', line))

    reins[deer] = list([int(i) for i in nums])

total_time = 2503

# Part 1
race_stats = {}

for deer, nums in reins.items():
    speed, duration, rest = nums
    lap_time = duration + rest

    rem_time = total_time % lap_time
    run_time = total_time // lap_time

    run_distance = speed * (run_time * duration)

    if rem_time > duration:
        run_distance += speed * duration

    race_stats[deer] = run_distance

solution_1 = max(race_stats.values())
print(f"Part 1: {solution_1}")


# Part 2
reins = [Reindeer(key, *value) for key, value in reins.items()]

for _ in range(2503):
    best = []

    for r in reins:
        r.move()

        if best == []:
            best.append(r)

        else:
            if r.dist > best[0].dist:
                best = [r]

            elif r.dist == best[0].dist:
                best.append(r)

            else:
                pass

    for b in best:
        b.point += 1

print(f"Part 2: {max(r.point for r in reins)}")

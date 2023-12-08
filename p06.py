import re

text = """Time:      7  15   30
Distance:  9  40  200"""

text2 = """Time:        62     73     75     65
Distance:   644   1023   1240   1023"""

lines = [s.strip() for s in text2.split("\n")]

def parse(lines):
    times = [int(x) for x in re.split(r"\s+", re.split(r":\s+", lines[0])[1])]
    distances = [int(x) for x in re.split(r"\s+", re.split(r":\s+", lines[1])[1])]

    return (times, distances)

(times, distances) = parse(lines)

final = 1
for i in range(0, len(times)):
    max_t = times[i]
    ctr = 0
    for hold_t in range(0, max_t):
        speed = hold_t
        dist_traveled = speed * (max_t - hold_t)
        if dist_traveled > distances[i]:
            ctr += 1 
    print(ctr)
    final = final * ctr

print(final)

# part 2
# final = 1
max_t = int("".join(str(s) for s in times))
max_d = int("".join(str(s) for s in distances))

ctr = 0
for hold_t in range(0, max_t):
    speed = hold_t
    dist_traveled = speed * (max_t - hold_t)
    if dist_traveled > max_d:
        ctr += 1 
print(ctr)



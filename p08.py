from math import lcm

text = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

lines = text.split("\n")
lines = [s.strip() for s in open("p08.txt").readlines()]

instructions = lines[0]
nodes_text = lines[2:]
nodes = {}

for n in nodes_text:
    st = n[0:3]
    left = n[7:10]
    right = n[12:15]

    nodes[st] = (left, right)

cur = [n for n in nodes if n[2] == 'A']

def iterate(curr, i):
    targets = []
    history = set()

    while (curr, i % len(instructions)) not in history:
        # haven't looped around yet
        history.add((curr, i % len(instructions)))
        
        step = instructions[i % len(instructions)]
        if step == "L": curr = nodes[curr][0]
        elif step == "R": curr = nodes[curr][1]
        else: print("unknown instruction " + step)

        i += 1
        if curr[2] == 'Z': targets.append(i)

    return(targets)

final = []
for n in cur:
    steps = iterate(n, 0)
    print(steps)
    for s in steps: final.append(s)

print(lcm(*final))
    


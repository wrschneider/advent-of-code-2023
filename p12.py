text = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

lines = text.split("\n")
lines = [line.strip() for line in open("p12.txt").readlines()]
rows = [line.split() for line in lines]
parsed = [(r[0], [int(x) for x in r[1].split(",")]) for r in rows]

d = {}

def block_placements(line, start, next_block_len):
    for i in range(start, len(line) - next_block_len + 1):
        if all(line[j] in "?#" for j in range(i, i + next_block_len)):
            if i + next_block_len >= len(line) or line[i + next_block_len] != "#":
                yield i
        if line[i] == "#": # not an option, next block must start here
            break

def count_solutions(rec, start=0, start_block=0, bps=[]):
    if (start, start_block) in d:
        return d[start, start_block]

    (line, blocks) = rec

    count = 0
    next_block_len = blocks[start_block]
    for bp in block_placements(line, start, next_block_len):
        # did we place the last block?
        if start_block >= len(blocks) - 1:
            # not a valid solution
            if any(line[i] == "#" for i in range(bp + next_block_len, len(line))):
                continue
            # valid solution, increment counter
            else:
                count += 1
        else:
            # more blocks, recurse
            count += count_solutions(rec, bp + next_block_len + 1, start_block + 1, bps + [bp])

    d[start, start_block] = count
    return count

ctr = 0
for p in parsed:
    d = {}
    gs = count_solutions(p)
    print(gs)
    ctr += gs
print(ctr)

ctr = 0
for p in parsed:
    d = {}
    p2 = ("?".join([p[0] for i in range(0,5)]), p[1] * 5)
    gs = count_solutions(p2)
    print(gs)
    ctr += gs
print(ctr)

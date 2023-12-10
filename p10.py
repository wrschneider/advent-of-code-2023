# simple loop
text = """.....
.S-7.
.|.|.
.L-J.
....."""

# simple loop with clutter
text2 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

# more complex loop
text3 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

lines = text.split("\n")
lines = [s.strip("\n") for s in open("p10.txt").readlines()]

def find_s(lines):
    for i in range(0, len(lines)):
        line = lines[i]
        for j in range(0, len(line)):
            if line[j] == 'S': return (i, j)

# return two possible next tiles from S
def next_from_start(lines, s):
    (si, sj) = s
    next_tiles = []
    # can you go up?
    if si > 0 and lines[si-1][sj] in "|7F":
        next_tiles.append((si-1, sj))
    # down?
    if si < len(lines) and lines[si+1][sj] in "|JL":
        next_tiles.append((si+1, sj))
    # left
    if sj > 0 and lines[si][sj-1] in "-LF":
        next_tiles.append((si, sj-1))
    if sj < len(lines[0]) and lines[si][sj+1] in "-J7":
        next_tiles.append((si, sj+1))
    return next_tiles

def next_from_here(lines, curr, prev):
    print(curr,prev)
    (si, sj) = curr
    (pi, pj) = prev
    curr_tile = lines[si][sj]

    if curr_tile in "|LJ":
        # these tiles allow going up
        if si > 0 and pi != si-1:
            up_tile = lines[si-1][sj]
            if up_tile in "|F7S": return (si-1, sj)
    if curr_tile in "|F7":
        # these allow going down
        if si < len(lines) and pi != si+1:
            down_tile = lines[si+1][sj]
            if down_tile in "|LJS": return (si+1, sj)
    
    if curr_tile in "-7J":
        # these allow going left
        if sj > 0 and pj != sj-1:
            left_tile = lines[si][sj-1]
            if left_tile in "-FLS": return (si, sj-1)

    if curr_tile in "-FL":
        # these allow going right
        if sj < len(lines[si]) and pj != sj+1:
            right_tile = lines[si][sj+1]
            if right_tile in "-7JS": return (si, sj+1)

s = find_s(lines)

print(s)
n = next_from_start(lines, s)
loop = [s, n[0]]
while loop[-1] != s:
    next1 = next_from_here(lines, loop[-1], loop[-2])
    loop.append(next1)
    
print(loop)
loop_set = set(loop)

cleansed_grid = []
for i in range(0, len(lines)):
    st = ""
    for j in range(0, len(lines[0])):
        if (i, j) in loop_set: 
            st = st + lines[i][j]
        else:
            st = st + "."
    cleansed_grid.append(st)
                
print(len(lines), len(lines[0]))
# confirmed 140x140 (19600 squares total)
# upper bound as total # of non-loop tiles (5428)

ctr = 0
for i in range(0, len(lines)):
    inside = False
    st = ""
    started = ""
    for ch in cleansed_grid[i]:
        if ch == ".":
            st += ("I" if inside else "O")
            if inside: ctr += 1
        elif ch == "|" or ch == "S": # special case, hardwired
            inside = not inside
            st += ch
        elif ch == "F":
            started = "F"
            st += ch
        elif ch == "L":
            started = "L"
            st += ch
        elif ch == "J":
            if started == "F": 
                inside = not inside
                started = ""
            st += ch
        elif ch == "7":
            if started == "L":
                inside = not inside
                started = ""
            st += ch
        elif ch == "-":
            st += ch
    print(st)

print(ctr)
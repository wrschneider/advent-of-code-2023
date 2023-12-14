text = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

lines = text.split("\n")
lines = [s.strip() for s in open("p11.txt").readlines()]
empty_rows = set()
empty_cols = set()

for i in range(0, len(lines)):
    if all(ch == "." for ch in lines[i]): empty_rows.add(i)

for j in range(0, len(lines[0])):
    if all(lines[i][j] == "." for i in range(0, len(lines))): empty_cols.add(j)

# find galaxies
galaxies = []
for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if lines[i][j] == "#": galaxies.append((i,j))

expansion_factor = 1000000-1

total = 0
for i in range(0, len(galaxies)):
    for j in range(i, len(galaxies)):
        (g1r, g1c) = galaxies[i]
        (g2r, g2c) = galaxies[j]

        (bigr, smallr) = (g1r, g2r) if g1r >= g2r else (g2r, g1r)
        (bigc, smallc) = (g1c, g2c) if g1c >= g2c else (g2c, g1c)

        empty_rows_between = len([x for x in empty_rows if x in range(smallr, bigr)])
        empty_cols_between = len([x for x in empty_cols if x in range(smallc, bigc)])
        
        dist = bigr - smallr + bigc - smallc + empty_rows_between * expansion_factor + empty_cols_between * expansion_factor 
        # print(i, j, dist)
        total += dist

print(total)

        





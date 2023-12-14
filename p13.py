text = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

lines = text.split("\n")
lines = [s.strip() for s in open("p13.txt")]

# i=1: 0->1     2-
# i=2: 0->3, 1->2
# 0->5, 1->4, 2->3  
# 0->7, 1->6, 2->5, 3->4 
def find_reflection(m):
    width = len(m[0])
    MISMATCH = 1
    for i in range(1, width):
        mismatch = sum(1 for r in range(0, len(m)) for j in range(max(0, i*2-width), i) if m[r][j] != m[r][2*i - (j+1)])
        if mismatch == MISMATCH:
            return i

    for i in range(1, len(m)):
        mismatch = sum(1 for c in range(0, width) for j in range(max(0, i*2-len(m)), i) if m[j][c] != m[2*i - (j+1)][c])
        if mismatch == MISMATCH:
            return i*100

    return 0

mirror = []
mirrors = [mirror]
for line in lines:
    if line:
        mirror.append(line)
    else: 
        mirror = []
        mirrors.append(mirror)

print(sum(find_reflection(m) for m in mirrors))
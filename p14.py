from collections import Counter

text = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

lines = [list(s) for s in text.split("\n")]
lines = [list(s.strip()) for s in open("p14.txt").readlines()]

def run_cycle(lines):
    # North
    for col in range(0, len(lines[0])):
        for row in range(0, len(lines)):
            if lines[row][col] == ".":
                for row2 in range(row + 1, len(lines)):
                    if lines[row2][col] == "#": break # nothing left to move
                    if lines[row2][col] == "O":
                        # move it
                        lines[row2][col] = "."
                        lines[row][col] = "O"
                        break
    
    # West
    for row in range(0, len(lines)):
        for col in range(0, len(lines[0])):
            if lines[row][col] == ".":
                for col2 in range(col + 1, len(lines[0])):
                    if lines[row][col2] == "#": break # nothing left to move
                    if lines[row][col2] == "O":
                        # move it
                        lines[row][col2] = "."
                        lines[row][col] = "O"
                        break
    # South
    for col in range(0, len(lines[0])):
        for row in range(len(lines) - 1, -1, -1):
            if lines[row][col] == ".":
                for row2 in range(row - 1, -1, -1):
                    if lines[row2][col] == "#": break # nothing left to move
                    if lines[row2][col] == "O":
                        # move it
                        lines[row2][col] = "."
                        lines[row][col] = "O"
                        break

    # East
    for row in range(0, len(lines)):
        for col in range(len(lines[0]) - 1, -1, -1):
            if lines[row][col] == ".":
                for col2 in range(col - 1, -1, -1):
                    if lines[row][col2] == "#": break # nothing left to move
                    if lines[row][col2] == "O":
                        # move it
                        lines[row][col2] = "."
                        lines[row][col] = "O"
                        break

def summarize(lines):
    return "\n".join("".join(line) for line in lines)

summaries = [summarize(lines)]
cycle = None    
for i in range(0, 1000000000):
    run_cycle(lines)
    s = summarize(lines)
    for j in range(0, len(summaries)):
        if s == summaries[j]:
            print("Stopping!", i, j)
            cycle = (i, j)
    summaries.append(s)
    score = 0
    for i2 in range(0, len(lines)):
        c = Counter(lines[i2])
        score += c["O"] * (len(lines) - i2)

    print(i, len(summaries) - 1, score)
    if cycle is not None:
        break

cycle_len = cycle[0] - cycle[1] + 1
print(cycle_len)
index = (1000000000 - cycle[1]) % cycle_len + cycle[1]
print(index)

lines = summaries[index].split("\n")

score = 0
for i in range(0, len(lines)):
    c = Counter(lines[i])
    score += c["O"] * (len(lines) - i)

print(score)
# tried and failed 101016, 101033, 101003, 101017
# 101010 right answer 

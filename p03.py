text = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

lines = [s.strip() for s in text.split("\n")]

lines = [s.strip() for s in open("p03.txt").readlines()]

def is_symbol(c):
    return not (c.isdigit() or c == ".")

def is_adjacent_to_symbol(lines, r, c1, c2):
    for i in range(max(r - 1, 0), min(r + 2, len(lines))):
        for j in range(max(c1 - 1, 0), min(c2 + 1, len(lines[0]))):
            if is_symbol(lines[i][j]): return True
    return False
    
def find_gears(lines, number_coordinates):
    for r in range(0, len(lines)):
        row = lines[r]
        for c in range(0, len(lines)):
            if lines[r][c] == "*":
                # maybe a gear, check overlapping numbers
                overlapping = []
                for nc in number_coordinates:
                    (nr, nc1, nc2) = nc
                    if nr in range(r - 1, r + 2) and c in range(nc1 - 1, nc2 + 1):
                        overlapping.append(int(lines[nr][nc1:nc2]))
                # print(overlapping)
                if len(overlapping) == 2:
                    yield(overlapping[0] * overlapping[1])
                

def find_numbers(lines):
    for r in range(0, len(lines)):
        row = lines[r]
        c = 0
        while c < len(row):
            if row[c].isdigit():
                # found digit
                c2 = c + 1
                while c2 < len(row) and row[c2].isdigit():
                    c2 += 1
                yield(r, c, c2)
                c = c2
            else: c += 1

number_coordinates = [nc for nc in find_numbers(lines)]

print(sum(int(lines[r][c:c2]) for (r, c, c2) in number_coordinates if is_adjacent_to_symbol(lines, r, c, c2)))
# for nc in number_coordinates: print(nc)
print(sum(g for g in find_gears(lines, number_coordinates)))


text = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""

lines = text.split("\n")
lines = [s.strip() for s in open("p16.txt").readlines()]

height = len(lines)
width = len(lines[0])


def in_bounds(next_pos):
    return next_pos[0] >= 0 and next_pos[1] >= 0 and next_pos[0] < height and next_pos[1] < width


def test_beam(init_pos, init_dir):
    # beam status = ((r, c), (dr, dc))
    beams = [(init_pos, init_dir)]
    visited = set(beams)

    energized = set()
    while beams:
        beam = beams.pop()
        visited.add(beam)
        # where do you go next?
        (pos, dir) = beam
        (r, c) = pos

        energized.add(pos)
        # TODO fix copy-paste
        if lines[r][c] == "." or lines[r][c] == "-" and dir[0] == 0 or lines[r][c] == "|" and dir[1] == 0:
            next_pos = (r + dir[0], c + dir[1])
            if in_bounds(next_pos) and (next_pos, dir) not in visited:
                beams.append((next_pos, dir))
        elif lines[r][c] in "/\\":
            next_dir = (-dir[1], -dir[0]) if lines[r][c] == "/" else (dir[1], dir[0])
            next_pos = (r + next_dir[0], c + next_dir[1])
            if in_bounds(next_pos) and (next_pos, next_dir) not in visited:
                beams.append((next_pos, next_dir))
        elif lines[r][c] in "-|":
            next_dirs = [(1, 0), (-1, 0)] if lines[r][c] == "|" else [(0, 1), (0, -1)]
            for i in range(0, 2):
                next_dir = next_dirs[i]
                next_pos = (r + next_dir[0], c + next_dir[1])
                if in_bounds(next_pos) and (next_pos, next_dir) not in visited:
                    beams.append((next_pos, next_dir))
        
    return len(energized)

# max starting from left edge?
print(max(test_beam((r, 0), (0, 1)) for r in range(0, height)))
# from right?
print(max(test_beam((r, width-1), (0, -1)) for r in range(0, height)))
# from top?
print(max(test_beam((0, c), (1, 0)) for c in range(0, width)))
# bottom?
print(max(test_beam((height-1, c), (-1, 0)) for c in range(0, width)))
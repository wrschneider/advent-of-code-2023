import re

text = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

lines = [s.strip() for s in text.split("\n")]

lines = [s.strip() for s in open("p02.txt").readlines()]

maxes = {"red": 12, "green": 13, "blue": 14}

def cubes_possible(c):
    colors = c.split(", ")
    for color in colors:
        (num, color_name) = color.split(" ")
        if int(num) > maxes[color_name]: return False

    return True

def cubes_required(c):
    colors = c.split(", ")
    d = {"red": 0, "green": 0, "blue": 0}
    for color in colors:
        (num, color_name) = color.split(" ")
        d[color_name] = int(num)

    return d

def min_cubes_for_game(s):
    turns = s.split(": ")[1].split("; ") # don't care about ID
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for t in turns:
        min_turn_cubes = cubes_required(t)
        for color in min_turn_cubes:
            if min_turn_cubes[color] > min_cubes[color]:
                min_cubes[color] = min_turn_cubes[color]
    
    return min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]

# return id if possible else 0
def game_possible(s):
    (game_id, cubes) = s.split(": ")
    id = int(game_id.split(" ")[1])
    if all(cubes_possible(c) for c in cubes.split("; ")):
        return id
    else:
        return 0


# print(sum(game_possible(s) for s in lines))
print(sum(min_cubes_for_game(s) for s in lines))
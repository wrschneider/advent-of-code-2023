import re

text = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

lines = [s.strip() for s in text.split("\n")]

lines = [s.strip() for s in open("p04.txt").readlines()]

def count_matches(s):
    after_colon = s.split(":")[1]
    (winning_str, card_str) = [ss.strip() for ss in after_colon.split("|")]
    winning_nums = [n.strip() for n in re.split(r'\s+', winning_str)]
    card_nums = [n.strip() for n in re.split(r'\s+', card_str)]

    match_count = sum(1 for num in card_nums if num in winning_nums)
    return match_count

def score_line(s):
    match_count = count_matches(s)
    if match_count > 0: return 2 ** (match_count - 1)
    return 0

def count_instances(lines, i, copies):
    matches = count_matches(lines[i])
    for j in range(i+1, i+1+matches):
        if j < len(copies): copies[j] += copies[i]
    print(copies)

print(sum(score_line(line) for line in lines))

copies = [1] * len(lines)
for i in range(0, len(lines)): count_instances(lines, i, copies)

print(sum(copies))


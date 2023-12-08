import functools
from collections import Counter

text = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

lines = [s.strip() for s in text.split("\n")]
lines = [s.strip() for s in open("p07.txt").readlines()]

hands_str = [ln.split(" ") for ln in lines]
hands = [(s[0], int(s[1])) for s in hands_str]

def htype_old(hand):
    grouped = Counter(list(hand)).most_common()
    if grouped[0][1] == 5:
        return 0
    elif grouped[0][1] == 4:
        return 1
    elif grouped[0][1] == 3:
        if grouped[1][1] == 2:
            return 2
        else: return 3
    elif grouped[0][1] == 2:
        if grouped[1][1] == 2:
            return 4
        else: return 5
    else: return 6

def htype(hand):
    c = Counter(list(hand))
    jokers = c.get('J', 0)
    del c['J']
    grouped = c.most_common()
    if jokers == 5 or grouped[0][1] + jokers == 5:
        return 0
    elif jokers == 4 or grouped[0][1] + jokers == 4:
        return 1
    elif grouped[0][1] + jokers == 3:
        if grouped[1][1] == 2:
            return 2
        else: return 3
    elif grouped[0][1] + jokers == 2:
        if grouped[1][1] == 2:
            return 4
        else: return 5
    else: return 6

# cards = "23456789TJQKA"
cards = "J23456789TQKA"
print(htype('K9J8J'))

def compare(h1, h2):
    t1 = htype(h1[0])
    t2 = htype(h2[0])
    if t1 < t2: return -1
    if t1 > t2: return 1
    # break tie
    for i in range(0, 5):
        c1 = cards.find(h1[0][i])
        c2 = cards.find(h2[0][i])
        if c1 > c2: return -1
        if c1 < c2: return 1
    return 0

hands.sort(key=functools.cmp_to_key(compare))

# for h in hands: print(h)
score = 0
for i in range(0, len(hands)):
    rank = (len(hands) - i)
    score += hands[i][1] * rank

print(score)
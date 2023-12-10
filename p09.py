text = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

lines = text.split("\n")
lines = [s.strip() for s in open("p09.txt").readlines()]

histories = [[int(x) for x in line.split()] for line in lines]

# parse differences for one line
def parse_differences(hist):
    print(hist)
    hist_list = [hist]

    while any(x != 0 for x in hist):
        diffs = [(hist[i+1] - hist[i]) for i in range(0, len(hist)-1)]
        hist = diffs
        hist_list.append(hist)
    return hist_list

def prediction(hist_list):
    val = 0
    for i in range(1, len(hist_list)):
        j = len(hist_list) - i - 1
        val = val + hist_list[j][-1]

    return val

def prediction_back(hist_list):
    val = 0
    for i in range(1, len(hist_list)):
        j = len(hist_list) - i - 1
        val = hist_list[j][0] - val

    return val

def predict(hist):
    return prediction_back(parse_differences(hist))

print(sum(predict(h) for h in histories))

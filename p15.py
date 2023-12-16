line = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

line = open("p15.txt").readlines()[0].strip()
codes = line.split(",")

def hash(s):
    ctr = 0
    for ch in s:
        ctr += ord(ch)
        ctr *= 17
        ctr = ctr % 256
    return ctr

boxes = []
for i in range(0, 256): boxes.append([])

def process_box(boxes, s):
    if s.endswith("-"):
        label = s[0:-1]
        i = hash(label)
        box = boxes[i]

        for j in range(0, len(box)):
            if box[j].split("=")[0] == label:
                boxes[i] = box[0:j] + box[(j + 1):]
                break
    
    elif "=" in s:
        label = s.split("=")[0]
        i = hash(label)
        box = boxes[i]

        for j in range(0, len(box)):
            if box[j].split("=")[0] == label:
                boxes[i] = box[0:j] + [s] + box[(j + 1):]
                break
        box.append(s)
    else:
        print("WTF", s)

for s in codes:
    print("")
    process_box(boxes, s)
    for box in boxes:
        if box: print(box)

print(sum(hash(s) for s in codes))

tot = 0
for i in range(0, 256):
    box = boxes[i]
    for j in range(0, len(box)):
        lens = box[j]
        focal = int(lens.split("=")[1])
        score = (i + 1) * (j + 1) * focal
        tot += score

print(tot)

# 46894 too low
# 5016079 too high
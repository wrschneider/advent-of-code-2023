text = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

text = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

lines = [s.strip() for s in text.split("\n")]
lines = open("p01.txt").readlines()

num_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def digits(s):
  print(s)
  first = None
  second = None
  for ch in s:
    if ch in "0123456789":
      if first is None: first = ch
      second = ch
  return int(first + second)

def digit_text(s):
  first = None
  second = None
  print (s)
  for i in range(len(s)):
    if s[i] in "0123456789":
      second = int(s[i])
      if first is None: first = second

    for j in range(len(num_digits)):
      if s[i:].startswith(num_digits[j]):
        second = j + 1
        if first is None: first = second
  print (first,second)
  return first * 10 + second

# total = sum(digits(s) for s in lines)
# print(total)

total2 = sum(digit_text(s) for s in lines)
print(total2)

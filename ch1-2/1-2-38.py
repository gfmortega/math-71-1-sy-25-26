name = input()
color = input()
age = int(input())
height = int(input())

tally = 0

if len(name) <= 5:
    tally += 1

if color[0] == 'B' or color[0] == 'b':
    tally += 1

if 20 <= age <= 25:
    tally += 1

if height >= 150:
    tally += 1

print(tally)

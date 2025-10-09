from itertools import product
base_STR = int(input())
threshold = int(input())

good_outcomes = 0
all_outcomes = 0
for rolls in product(range(1, 6+1), repeat=4):
    all_outcomes += 1
    if base_STR + sum(rolls) >= threshold:
        good_outcomes += 1

print(f'{good_outcomes/all_outcomes:.12f}')
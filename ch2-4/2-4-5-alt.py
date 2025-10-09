from itertools import combinations
n, b = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]

possible = []
for i, j in combinations(range(n), 2):
    if p[i] + p[j] <= b:
        possible.append((i+1, j+1))

print(len(possible))
for pair in possible:
    print(*pair)
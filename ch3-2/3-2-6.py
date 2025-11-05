r, c = [int(x) for x in input().split()]
grid = [
    [int(x) for x in input().split()]
    for _ in range(r)
]

for j in range(c):
    total = 0
    for i in range(r):
        total += grid[i][j]
    print(total)

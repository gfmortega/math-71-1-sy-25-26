N = 8
grid = [
    list(input())
    for _ in range(N)
]

x, y = None, None
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'N':
            x, y = i, j
            break

# all possible "one steps" a knight can take
dir = [
    (-2, -1),
    (-2, +1),
    (-1, -2),
    (-1, +2),
    (+1, -2),
    (+1, +2),
    (+2, -1),
    (+2, +1)
]

for dx, dy in dir:
    i = x + dx
    j = y + dy
    if 0 <= i < N and 0 <= j < N:
        grid[i][j] = '*'

for row in grid:
    print(''.join(row))
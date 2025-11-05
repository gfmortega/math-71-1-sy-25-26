N = 8
grid = [
    list(input())
    for _ in range(N)
]

x, y = None, None
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'K':
            x, y = i, j
            break

# all possible "one steps" a king can take
dir = [
    (-1, -1),
    (-1,  0),
    (-1, +1),
    ( 0, -1),
    ( 0, +1),
    (+1, -1),
    (+1,  0),
    (+1, +1),
]

for dx, dy in dir:
    i = x + dx
    j = y + dy
    if 0 <= i < N and 0 <= j < N:
        grid[i][j] = '*'

for row in grid:
    print(''.join(row))
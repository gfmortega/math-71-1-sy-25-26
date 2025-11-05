N = 8
grid = [
    list(input())
    for _ in range(N)
]

x, y = None, None
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'B':
            x, y = i, j
            break

dir = [
    (+1, +1),
    (+1, -1),
    (-1, -1),
    (-1, +1),
]
for di, dj in dir:
    i = x
    j = y
    while True:
        i += di
        j += dj
        if (
            not (0 <= i < N and 0 <= j < N) or
            grid[i][j] != '.'
        ):
            break
        else:
            grid[i][j] = '*'


for row in grid:
    print(''.join(row))
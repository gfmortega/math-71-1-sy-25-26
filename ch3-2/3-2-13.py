def horizontal_flip(grid):
    n = len(grid)

    ans = [
        [None for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            # grid[i][j] ---> ans[i][(n-1) - j]
            ans[i][(n-1) - j] = grid[i][j]
    return ans

def diagonal_flip(grid):
    n = len(grid)

    ans = [
        [None for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            # grid[i][j] ---> ans[j][i]
            ans[i][j] = grid[j][i]
    return ans

n = int(input())
grid = [
    [int(x) for x in input().split()]
    for _ in range(n)
]
command = input()

if command == 'clockwise':
    grid = horizontal_flip(diagonal_flip(grid))
elif command == 'counter-clockwise':
    grid = diagonal_flip(horizontal_flip(grid))
else:
    raise RuntimeError(f'Expected "clockwise" or "counter-clockwise", got {command}')

for row in grid:
    print(*row)
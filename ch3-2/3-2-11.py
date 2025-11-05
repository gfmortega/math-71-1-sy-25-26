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

def vertical_flip(grid):
    n = len(grid)

    ans = [
        [None for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            # grid[i][j] ---> ans[(n-1) - i][j]
            ans[(n-1) - i][j] = grid[i][j]
    return ans

n = int(input())
grid = [
    [int(x) for x in input().split()]
    for _ in range(n)
]
command = input()

if command == 'vertical':
    grid = vertical_flip(grid)
elif command == 'horizontal':
    grid = horizontal_flip(grid)
else:
    raise RuntimeError(f'Expected "vertical" or "horizontal", got {command}')

for row in grid:
    print(*row)
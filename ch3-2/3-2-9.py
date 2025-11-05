n = int(input())
grid = [
    input()
    for _ in range(n)
]

diag_letters = []
for i in range(n):
    # Let j be the value such that i = j
    j = i
    diag_letters.append(grid[i][j])
print(''.join(diag_letters))
n = int(input())
grid = [
    input()
    for _ in range(n)
]

anti_diag_letters = []
for i in range(n):
    # Let j be the value such that i + j = n-1
    j = (n-1) - i
    anti_diag_letters.append(grid[i][j])
print(''.join(anti_diag_letters))
n, b = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]

possible = []
for i in range(n):
    for j in range(i+1, n):
        # Forces only i < j

        if p[i] + p[j] <= b:
            possible.append((i+1, j+1))

print(len(possible))
for pair in possible:
    print(*pair)
n, m = [int(x) for x in input().split()]

friends = [0 for _ in range(n)]
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    u -= 1
    v -= 1

    friends[u] += 1
    friends[v] += 1

print(*friends)
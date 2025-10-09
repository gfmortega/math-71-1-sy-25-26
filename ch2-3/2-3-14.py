n, m = [int(x) for x in input().split()]

following_count = [0 for _ in range(n)]
followed_by_count = [0 for _ in range(n)]

for _ in range(m):
    u, v = [int(x) for x in input().split()]
    # conversion from 1-index to 0-index
    u -= 1
    v -= 1

    following_count[u] += 1
    followed_by_count[v] += 1

print(*following_count)
print(*followed_by_count)


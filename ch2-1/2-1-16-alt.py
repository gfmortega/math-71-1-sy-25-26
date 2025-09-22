n = int(input())
h = [int(x) for x in input().split()]

# make a list of size n; populate it with dummy elements first
good = [None for _ in range(n)]

# first pass, check the condition
for i in range(n):
    good[i] = (i-1 >= 0 and h[i-1] == h[i]) or (i+1 < n and h[i] == h[i+1])

# second pass, after all checks are done, apply the updates
for i in range(n):
    if good[i]:
        h[i] += 3 

print(*h)

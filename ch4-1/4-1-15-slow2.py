INF = 10**18

n = int(input())
a = [int(x) for x in input().split()]

running_max = -INF
for i in range(n):
    for j in range(i+1, n):
        running_max = max(running_max, abs(a[i] - a[j]))

print(running_max)
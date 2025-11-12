INF = 10**18

n = int(input())
a = [int(x) for x in input().split()]
a.sort()

smallest = INF
for i in range(n-1):
    candidate = a[i+1] - a[i]
    if candidate < smallest:
        smallest = candidate
print(smallest)
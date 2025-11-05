n = int(input())
locations = set([int(x) for x in input().split()])

q = int(input())
for _ in range(q):
    l, k = [int(x) for x in input().split()]

    total = 0
    for candidate in range(l-k, l+k+1):
        if candidate in locations:
            total += 1
    print(total)
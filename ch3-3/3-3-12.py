n = int(input())
locations = set([
    tuple([int(x) for x in input().split()])
    for _ in range(n)
])

q = int(input())
for _ in range(q):
    h, k, r = [int(x) for x in input().split()]

    total = 0
    for x in range(h-r, h+r+1):
        for y in range(k-r, k+r+1):
            if not((x - h)**2 + (y - k)**2 <= r):
                continue
            if (x, y) in locations:
                total += 1
    print(total)
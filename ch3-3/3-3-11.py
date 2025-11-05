n = int(input())
locations = [int(x) for x in input().split()]
freq = dict()
for location in locations:
    freq[location] += 1

q = int(input())
for _ in range(q):
    l, k = [int(x) for x in input().split()]

    total = 0
    for candidate in range(l-k, l+k+1):
        if candidate in freq:
            total += freq[candidate]
    print(total)
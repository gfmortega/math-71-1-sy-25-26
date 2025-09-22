n = int(input())
h = [int(x) for x in input().split()]

# Look at problem 2.1.16
# We didn't use its tech here, but this is still correct.  Why?

for i in range(n):
    # remember to be careful about index out of bounds
    if i+1 < n and h[i] < h[i+1]:
        h[i] -= 1

print(*h)

n = int(input())
a = input().split()

Q = int(input())
for _ in range(Q):
    i, j = [int(x) for x in input().split()]
    i -= 1
    j -= 1

    a[i], a[j] = a[j], a[i]

print(*a)
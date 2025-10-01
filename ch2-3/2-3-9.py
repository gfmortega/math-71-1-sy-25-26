n = int(input())
a = [int(x) for x in input().split()]

Q = int(input())
for _ in range(Q):
    L, R = [int(x) for x in input().split()]
    L -= 1
    R -= 1

    for i in range(L, R+1):
        a[i] += 1

print(*a)
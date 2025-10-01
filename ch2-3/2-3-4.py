s = list(input())

Q = int(input())
for _ in range(Q):
    i, x = input().split()
    i = int(i)

    s[i-1] = x

print(''.join(s))
n = int(input())
p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]

total = 0
for i in range(n):
    total += p[i]*q[i]

print(total)

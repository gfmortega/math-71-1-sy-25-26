n = int(input())
s = [int(x) for x in input().split()]

total = 0
for i in range(n):
    if s[i] == 7:
        total += s[i]
        if i-1 >= 0:
            total += s[i-1]
        if i+1 < n:
            total += s[i+1]
        

print(total)
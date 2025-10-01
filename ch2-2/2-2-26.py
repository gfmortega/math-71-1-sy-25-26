n = int(input())
s = [int(x) for x in input().split()]

total = 0
for i in range(n):
    if (
        s[i] == 7 or
        (i-1 >= 0 and s[i-1] == 7) or
        (i+1 < n and s[i+1] == 7)
    ):
        total += s[i]
        

print(total)
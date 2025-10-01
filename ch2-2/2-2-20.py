n = int(input())
price = [int(x) for x in input().split()]

# Find first day that price decreases
ans = None
for i in range(n):
    if i-1 >= 0 and price[i] < price[i-1]:
        ans = i+1  # because of 1-indexing
        break

if ans is None:
    print('no decrease')
else:
    print(ans)
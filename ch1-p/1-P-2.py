s = int(input())
e = int(input())
t = int(input())

# abs(s - e)
if s <= e:
    d = e - s
else:
    d = s - e

if t >= d and (t - d) % 2 == 0:
    print('Yes')
else:
    print('No')

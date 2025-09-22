n = int(input())
h = [int(x) for x in input().split()]

middle_children = []
for i in range(n):
    if (
        (0 <= i-1 and i+1 < n) and
        min(h[i-1], h[i+1]) < h[i] < max(h[i-1], h[i+1])
    ):
        middle_children.append(i+1)

if len(middle_children) > 0:
    print(*middle_children)
else:
    print('none')
h, k, r = [int(x) for x in input().split()]

points = []
for x in range(h-r, h+r+1):
    for y in range(k-r, k+r+1):
        if (x - h)**2 + (y - k)**2 <= r**2:
            points.append((x, y))

print(len(points))
for point in points:
    print(*point)
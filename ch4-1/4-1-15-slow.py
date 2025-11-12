n = int(input())
a = [int(x) for x in input().split()]

differences = []
for i in range(n):
    for j in range(i+1, n):
        differences.append(abs(a[i] - a[j]))

print(max(differences))
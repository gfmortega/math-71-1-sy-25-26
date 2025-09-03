n = int(input())
a = [int(x) for x in input().split()]
L, R = [int(x) for x in input().split()]

removed = a[:L-1] + a[R:]

average = sum(removed)/len(removed)
print(f'{average:.2f}')

n, s = [int(x) for x in input().split()]

def process_line(line):
    x, word2 = line.split()
    if word2 == 'change':
        return 0
    elif word2 == 'enter':
        return +int(x)
    elif word2 == 'leave':
        return -int(x)

ans = None
for i in range(n):
    delta = process_line(input())
    s += delta

    # Find the first time this s is 0
    if s == 0:
        ans = i+1
        break

if ans is None:
    print('always occupied')
else:
    print(f'hour {ans} is free')
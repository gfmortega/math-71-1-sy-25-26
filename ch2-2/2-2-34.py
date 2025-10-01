n = int(input())
dominos = [
    [int(x) for x in input().split()]
    for _ in range(n)
]

def good(domino0):
    endpoint = domino0[1]
    for domino in dominos[1:]:
        a, b = domino

        if a == endpoint:
            endpoint = b
        elif b == endpoint:
            endpoint = a
        else:
            return False
    return True

a0, b0 = dominos[0]
if good([a0, b0]) or good([b0, a0]):
    print('YES')
else:
    print('NO')
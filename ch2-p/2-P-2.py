def is_nice(n):
    for p in [2, 3, 5, 7]:
        while n % p == 0:
            n //= p
    return n == 1

T = int(input())
for _ in range(T):
    n = int(input())
    print(
        'nice'
        if is_nice(n)
        else 'not nice'
    )

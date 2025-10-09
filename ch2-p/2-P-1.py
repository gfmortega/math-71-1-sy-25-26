n = int(input())

k = 0
while not (n % 2 == 1):
    n //= 2
    k += 1

print(f'2**{k} x {n}')

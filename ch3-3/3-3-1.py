m = int(input())
mass_by_symbol = dict()
for _ in range(m):
    symbol, raw_mass = input().split()
    mass = float(raw_mass)
    mass_by_symbol[symbol] = mass

n = int(input())
total = 0
for _ in range(n):
    raw_qty, symbol = input().split()
    qty = int(raw_qty)
    total += qty * mass_by_symbol[symbol]

print(total)
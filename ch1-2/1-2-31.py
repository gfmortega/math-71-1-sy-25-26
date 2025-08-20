from math import pi
# pi = 3.141592653589793238462

k1 = int(input())
d1 = int(input())
k2 = int(input())
d2 = int(input())

# can cancel pi/2^2 from both sides of inequality
maguire_criterion = k1 * d1**2
holland_criterion = k2 * d2**2

if maguire_criterion > holland_criterion:
    print("Maguire's Pizza Parlor")
elif maguire_criterion < holland_criterion:
    print("Holland's Pizzeria")
else:
    print("Garfield's Lasagna")
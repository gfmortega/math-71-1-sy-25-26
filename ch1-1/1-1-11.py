a = float(input())
b = float(input())
c = float(input())

disc = (b**2 - 4*a*c)**0.5
root1 = (-b + disc) / (2*a)
root2 = (-b - disc) / (2*a)

print(f'{root1:.6f}')
print(f'{root2:.6f}')

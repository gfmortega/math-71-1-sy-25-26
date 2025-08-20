a = float(input())
b = float(input())

print(
    (a >= 150 and b >= 150)
    or
    (
        (a > 180 and b < 140) # Case 1: a is the tall one
        or
        (b > 180 and a < 140) # Case 2: b is the tall one
    )
)

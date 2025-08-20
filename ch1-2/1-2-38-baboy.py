name = input()
color = input()
age = int(input())
height = int(input())

a = len(name) <= 5
b = color[0] == 'B' or color[0] == 'b'
c = 20 <= age <= 25
d = height >= 150

if not (a or b or c or d):
    print(0)
elif (
    (a and not (b or c or d)) or
    (b and not (a or c or d)) or
    (c and not (a or b or d)) or
    (d and not (a or b or c))
):
    print(1)
elif (
    (a and b and not (c or d)) or
    (a and c and not (b or d)) or
    (a and d and not (b or c)) or
    (b and c and not (a or d)) or
    (b and d and not (a or c)) or
    (c and d and not (a or b))
):
    print(2)
elif (
    (a and b and c and not d) or
    (a and c and d and not b) or
    (a and b and d and not c) or
    (b and c and d and not a)
):
    print(3)
else:
    print(4)
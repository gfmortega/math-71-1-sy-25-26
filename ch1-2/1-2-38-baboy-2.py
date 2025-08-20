name = input()
color = input()
age = int(input())
height = int(input())

a = len(name) <= 5
b = color[0] == 'B' or color[0] == 'b'
c = 20 <= age <= 25
d = height >= 150

if a:
    if b:
        if c:
            if d:
                ans = 4
            else:
                ans = 3
        else:
            if d:
                ans = 3
            else:
                ans = 2
    else:
        if c:
            if d:
                ans = 3
            else:
                ans = 2
        else:
            if d:
                ans = 2
            else:
                ans = 1
else:
    if b:
        if c:
            if d:
                ans = 3
            else:
                ans = 2
        else:
            if d:
                ans = 2
            else:
                ans = 1
    else:
        if c:
            if d:
                ans = 2
            else:
                ans = 1
        else:
            if d:
                ans = 1
            else:
                ans = 0
print(ans)
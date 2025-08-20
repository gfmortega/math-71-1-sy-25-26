cmd = input()

if cmd == 'NEGATE':
    x = int(input())
    print(-x)
elif cmd == 'SUBTRACT':
    x = int(input())
    y = int(input())
    print(x - y)
elif cmd == 'MIN':
    x = int(input())
    y = int(input())
    z = int(input())

    if x <= y and x <= z:
        print(x)
    elif y <= x and y <= z:
        print(y)
    else:
        print(z)

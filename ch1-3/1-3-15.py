n = int(input())
rooms = input().split()
sentence = input().split()

direction = sentence[-1][:-1]
i = int(sentence[3][:-2])

if i > n:
    print(-1)
elif direction == 'left':
    print(rooms[i-1])
elif direction == 'right':
    print(rooms[-i])
else:
    raise RuntimeError("unexpected case")
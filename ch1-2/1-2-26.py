line = input()
k = int(input())

if k <= 0:
    print('Invalid k.')
elif len(line) > k:
    print(f'{line[:k]}...')
    print('The message was cut off because it was too long!')
else:
    print(line)
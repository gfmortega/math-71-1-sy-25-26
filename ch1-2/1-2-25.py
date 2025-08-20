line = input()

if len(line) > 10:
    print(f'{line[:10]}...')
    print('The message was cut off because it was too long!')
else:
    print(line)
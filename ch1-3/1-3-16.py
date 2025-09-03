words = input().split()

castle = words[-1][:-1]

not_count = len(words) - 5

# then, flip the answer!
if not_count % 2 == 1:
    if castle == 'A':
        castle = 'B'
    elif castle == 'B':
        castle = 'A'
    else:
        raise RuntimeError('Impossible case')

print(castle)
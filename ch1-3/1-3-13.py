sentence = input().split()

x = float(sentence[0])
y = float(sentence[-1][:-1])

comparison = sentence[2]
if comparison == 'less':
    check = x < y
elif comparison == 'greater':
    check = x > y
else:
    raise RuntimeError(f'got {comparison}, expected "less" or "greater" only')

if check:
    print('Correct')
else:
    print('Incorrect')
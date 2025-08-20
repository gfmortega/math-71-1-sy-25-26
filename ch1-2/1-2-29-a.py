n = input()

d = n[-1]
t = n[-2:]
if t == '11' or t == '12' or t == '13':
    suffix = 'th'
elif d == '1':
    suffix = 'st'
elif d == '2':
    suffix = 'nd'
elif d == '3':
    suffix = 'rd'
else:
    suffix = 'th'

print(f'{n}{suffix}')
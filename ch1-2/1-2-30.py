verb = input()

c = verb[0]

if c == 'b' or c == 'p':
    prefix = 'pam'
elif (
    c == 'd' or
    c == 'l' or
    c == 'r' or
    c == 's' or
    c == 't'
):
    prefix = 'pan'
elif (
    c == 'a' or
    c == 'e' or
    c == 'i' or
    c == 'o' or
    c == 'u'
):
    prefix = 'pang-'
else:
    prefix = 'pang'

print(f'{prefix}{verb}')
def complement(c):
    if c == 'G':
        return 'C'
    elif c == 'C':
        return 'G'
    elif c == 'A':
        return 'T'
    elif c == 'T':
        return 'A'

def is_complementary(x, y):
    return x == complement(y)

s = input()
t = input()

errors = 0
for i in range(len(s)):
    if not is_complementary(s[i], t[i]):
        errors += 1

if errors == 0:
    print("YES")
else:
    print("NO")
    print(errors)
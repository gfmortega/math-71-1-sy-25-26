def phi(w):
    ans = []
    for c in w:
        if c == 'a':
            ans.append('ab')
        elif c == 'b':
            ans.append('a')
        else:
            raise RuntimeError("Impossible case")
    return "".join(ans)

n = int(input())

word = 'a'
while not (len(word) >= n):
    word = phi(word)

print(word[:n])
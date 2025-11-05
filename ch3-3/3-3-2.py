sentence = input().split()

n = int(input())
banned_words = set([input() for _ in range(n)])

censored = []
for word in sentence:
    if word in banned_words:
        censored.append('*'*len(word))
    else:
        censored.append(word)

print(*sentence)

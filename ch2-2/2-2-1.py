n, a = input().split()
n = int(n)
words = input().split()

total = 0
for word in words:
    if word[0] == a:
        total += 1
print(total)

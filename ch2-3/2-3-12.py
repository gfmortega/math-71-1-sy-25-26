p, x = [int(x) for x in input().split()]

balance = p
days = 0
while not (balance >= x):
    balance += balance // 100
    days += 1

print(days)

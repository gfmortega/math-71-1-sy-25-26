name1 = input()
price1 = int(input())
name2 = input()
price2 = int(input())
name3 = input()
price3 = int(input())

if price1 > price2 + price3:
    print('Yes')
    print(name1)
elif price2 > price1 + price3:
    print('Yes')
    print(name2)
elif price3 > price1 + price2:
    print('Yes')
    print(name3)
else:
    print('No')

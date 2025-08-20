diameter = input()
edge = input()
plant = input()

count1 = 0
count5 = 0
count10 = 0

if diameter == '23':
    count1 += 1
elif diameter == '25':
    count5 += 1
elif diameter == '27':
    count10 += 1

if edge == 'segmented':
    count1 += 1
elif edge == 'plain':
    count5 += 1
elif edge == 'reeded':
    count10 += 1

if plant == 'waling-waling':
    count1 += 1
elif plant == 'tayabak':
    count5 += 1
elif plant == 'kapa-kapa':
    count10 += 1


if count1 >= 2:
    print(1)
elif count5 >= 2:
    print(5)
elif count10 >= 2:
    print(10)
else:
    print("CAN'T TELL")
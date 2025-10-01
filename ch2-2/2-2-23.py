n, x = [int(x) for x in input().split()]
players = []
for _ in range(n):
    name, raw_num = input().split()
    players.append((name, int(raw_num)))

# Identify the names of all people who submitted x
people_who_wrote_x = []
for name, num in players:
    if num == x:
        people_who_wrote_x.append(name)

if len(people_who_wrote_x) == 1:
    print(people_who_wrote_x[0])
else:
    print('no winner')

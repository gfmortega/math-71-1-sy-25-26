n, k = [int(x) for x in input().split()]
people = input().split()

vip = people[k-1]
people.pop(k-1)
people.insert(0, vip)

print(' '.join(people))
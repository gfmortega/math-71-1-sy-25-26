n = int(input())
h = [int(x) for x in input().split()]

# have to copy lists like this, otherwise we would
#  just have a reference to the same list h
new_h = list(h)

for i in range(n):
    # remember to be careful about index out of bounds
    if (i-1 >= 0 and h[i-1] == h[i]) or (i+1 < n and h[i] == h[i+1]):
        # since the condition involves checking the neighbors,
        #  modifying the list as you iterate over it 
        #  could cause errors!
        new_h[i] += 3

print(*new_h)

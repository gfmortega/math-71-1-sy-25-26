n = int(input())
h = [int(x) for x in input().split()]

# This does not work!
# The x in each loop iteration is a separate variable
#  that is different from the elements of h

# for x in h:
#     x += 1

# Access by index instead, to update
# We could use len(h), but by problem specs we 
#  are guaranteed the length is n
for i in range(n):
    h[i] += 1

print(*h)

Q, v = [int(x) for x in input().split()]

# This use of range is an idiom, i.e. a "set expression"
#   for "Run this code <Q> times"
# The use of _ communicates that this variable doesn't matter
for _ in range(Q):
    # This is just chapter 1 problem, but run Q times
    # But we can use the same v at the start for all loop iterations
    n = int(input())

    # if n % 2 == v % 2:
    #     res = "SAME"
    # else:
    #     res = "DIFFERENT"
    # print(res)

    # new syntax for fun: the ternary operator
    # equivalent to the above
    print("SAME" if n % 2 == v % 2 else "DIFFERENT")

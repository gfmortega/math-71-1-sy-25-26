Q = int(input())

# This use of range is an idiom, i.e. a "set expression"
#   for "Run this code <Q> times"
# The use of _ communicates that this variable doesn't matter
for _ in range(Q):
    # This is just chapter 1 problem, but run Q times
    n = int(input())

    # if n % 2 == 1:
    #     res = "ODD"
    # else:
    #     res = "EVEN"
    # print(res)

    # new syntax for fun: the ternary operator
    # equivalent to the above
    print("ODD" if n % 2 == 1 else "EVEN")

bottles = int(input())
pack_qty = int(input())
cost_per_indiv = int(input())
cost_per_pack = int(input())

# check if pack of m is better at all, vs
#  just buying a bottle m times
# If worse, never buy packs, indiv. only
if cost_per_pack > pack_qty*cost_per_indiv:
    print(bottles * cost_per_indiv)
else:
    full_packs = bottles // pack_qty
    leftovers = bottles % pack_qty

    # Check which is better:
    #  Buying 1 pack of m, or
    #  Buying "leftovers" indiv. pieces
    optionA = cost_per_pack * 1
    optionB = cost_per_indiv * leftovers
    if optionA < optionB:
        last_bit = optionA
    else:
        last_bit = optionB

    print(full_packs*cost_per_pack + last_bit)
def perform_faro_shuffle(deck):
    n = len(deck)
    if n % 2 != 0:
        raise RuntimeError(f"{n} is not even")
    
    top_half = deck[:n//2]
    bot_half = deck[n//2:]
    ans = []
    for i in range(n//2):
        ans.append(top_half[i])
        ans.append(bot_half[i])
    return ans

n = int(input())
deck = list(range(n))  # doesnt matter, any sequence of n distinct elements works
original_order = list(deck)

shuffles = 1
deck = perform_faro_shuffle(deck)
while deck != original_order:
    deck = perform_faro_shuffle(deck)

    shuffles += 1

print(shuffles)
red_stones = 10
blue_stones = 10
curr_player = "Alice"

while True:
    print(f"It's {curr_player}'s turn.")
    print(f"There are {red_stones} red stones and {blue_stones} blue stones left.")
    print("Type an action in the form <color> <number>")
    color, number = input().split()
    number = int(number)
    if color == "red":
        red_stones -= number
    else:
        blue_stones -= number
    if red_stones == 0 and blue_stones == 0:
        print(f"{curr_player} wins!")
        break
    else:
        if curr_player == "Alice":
            curr_player = "Bob"
        else:
            curr_player = "Alice"
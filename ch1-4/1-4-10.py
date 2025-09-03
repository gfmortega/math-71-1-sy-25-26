already_pushed = False

def button_push_reward():
    global already_pushed
    if already_pushed:
        return 0
    else:
        already_pushed = True
        return 100
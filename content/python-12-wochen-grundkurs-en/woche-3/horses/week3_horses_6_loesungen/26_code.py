stable_door_locked = True
right_key = False
if stable_door_locked:
    print("The stable door is locked.")
    if right_key:
        print("The key fits - the stable door opens!")
    else:
        print("This key does not fit.")
else:
    print("The stable door is already open.")
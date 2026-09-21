door_locked = True
right_key = False
if door_locked:
    print("The door is locked.")
    if right_key:
        print("The door opens!")
    else:
        print("This key does not fit.")
else:
    print("The door is already open.")

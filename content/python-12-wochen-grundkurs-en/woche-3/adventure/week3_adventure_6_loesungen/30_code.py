door_locked = False
right_key = True
if door_locked:
    print("The door is locked.")
    if right_key:
        print("The key fits - the door opens!")
    else:
        print("This key does not fit.")
else:
    print("The door is already open.")
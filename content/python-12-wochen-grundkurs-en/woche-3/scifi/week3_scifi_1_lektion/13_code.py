# Example: The locked airlock
airlock_locked = True
right_code = True

if airlock_locked:
    print("🚪 The airlock is locked.")
    if right_code:
        print("🔑 The code is correct – the airlock opens!")
    else:
        print("❌ Wrong code! Access denied.")
else:
    print("🚪 The airlock is already open.")
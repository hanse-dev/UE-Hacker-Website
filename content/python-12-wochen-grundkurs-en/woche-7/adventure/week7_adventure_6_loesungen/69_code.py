types = ["Treasure room", "Trap", "Empty room"]
import random

rooms = [random.choice(types) for i in range(5)]
all_valid = True
for room in rooms:
    if room not in types:
        all_valid = False
print(f"Rooms: {len(rooms)}")
print(f"All valid: {all_valid}")

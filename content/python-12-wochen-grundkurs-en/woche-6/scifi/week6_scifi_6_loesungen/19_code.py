def create_hangars(num_hangars, slots_per_hangar):
    return [["free"] * slots_per_hangar for _ in range(num_hangars)]

def dock_shuttle(hangars, hangar, slot, shuttle):
    hangars[hangar][slot] = shuttle
    return hangars

hangars = create_hangars(3, 4)
hangars = dock_shuttle(hangars, 0, 0, "Falcon")
hangars = dock_shuttle(hangars, 0, 1, "Hummingbird")
hangars = dock_shuttle(hangars, 1, 0, "Stormbird")
hangars = dock_shuttle(hangars, 2, 0, "Cometchaser")

print("=== Hangar Overview ===")
for i, hangar in enumerate(hangars):
    print(f"Hangar {i+1}: {hangar}")

free_slots = sum(s == "free" for hangar in hangars for s in hangar)
print(f"Free slots: {free_slots}")

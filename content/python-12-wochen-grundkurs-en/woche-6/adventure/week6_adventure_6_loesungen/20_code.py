import random

# Step 1 – Create vault compartments
def create_compartments(num_compartments, slots_per_compartment):
    return [["empty"] * slots_per_compartment for _ in range(num_compartments)]

compartments = create_compartments(3, 4)

# Step 2 – Store treasures
def store_treasure(compartments, compartment_index, treasure_name):
    for i, slot in enumerate(compartments[compartment_index]):
        if slot == "empty":
            compartments[compartment_index][i] = treasure_name
            return True
    return False

store_treasure(compartments, 0, "Gold Bar")
store_treasure(compartments, 0, "Crystal Core")
store_treasure(compartments, 1, "Silver Crown")
store_treasure(compartments, 2, "Ruby Ring")
store_treasure(compartments, 2, "Sapphire Chain")

# Step 3 – Distribute guard strength
def distribute_guard_strength(compartments, total_guard_strength):
    occupancies = [len([t for t in c if t != "empty"]) for c in compartments]
    total = sum(occupancies) or len(compartments)
    return [round(total_guard_strength * (o / total), 1) if total > 0 else total_guard_strength / len(compartments) for o in occupancies]

guard_list = distribute_guard_strength(compartments, 300)

# Step 4 – Print overview
def show_overview(compartments):
    total_slots = sum(len(c) for c in compartments)
    print(f"=== VAULT OVERVIEW ===")
    for i, compartment in enumerate(compartments):
        treasures = [t for t in compartment if t != "empty"]
        print(f"  Compartment {i+1}: {treasures if treasures else 'empty'}")
    print(f"Compartments: {len(compartments)} | Total slots: {total_slots}")

show_overview(compartments)
print(f"Guard strength distribution: {guard_list}")

# Bonus – random break-in attempts and check
break_in_attempts = [80, 150, 250]
attempt = random.choice(break_in_attempts)
print(f"\nBreak-in attempt with strength: {attempt}")
compartment_index = 0
well_guarded = guard_list[compartment_index] >= attempt
print(f"Compartment {compartment_index+1} holds: {well_guarded}")

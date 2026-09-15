def create_stalls(num_stalls, horses_per_stall):
    return [["empty"] * horses_per_stall for _ in range(num_stalls)]

def assign_horse(stalls, stall_num, spot_num, horse):
    stalls[stall_num][spot_num] = horse
    return stalls

stable = create_stalls(4, 3)
stable = assign_horse(stable, 0, 0, "Thunder")
stable = assign_horse(stable, 0, 1, "Luna")
stable = assign_horse(stable, 1, 0, "Storm")

print("=== Stable Overview ===")
for i, stall in enumerate(stable):
    print(f"Stall {i+1}: {stall}")

free_spots = sum(p == "empty" for stall in stable for p in stall)
print(f"Free spots: {free_spots}")
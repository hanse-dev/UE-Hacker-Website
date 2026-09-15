# Step 1 – Identify technician
technician = "Chief Engineer Ryo"
technician_id = 5503

# Step 2 – Record energy blocks
num_blocks = 6
energy_per_block = 45.5

# Step 3 – Calculate total energy
total_energy = num_blocks * energy_per_block

print(f"Technician: {technician} (ID: {technician_id})")
print(f"Energy blocks: {num_blocks}")
print(f"Energy per block: {energy_per_block} TW")
print(f"Total energy: {total_energy} TW")

# Bonus
cooling_per_block = 12.0
total_cooling = num_blocks * cooling_per_block
print(f"Total cooling output: {total_cooling} MW")
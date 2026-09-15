# Step 1 – Record fleet (8 ships)
s1_name = "ISS Aurora"
s1_energy = 87
s2_name = "ISS Titan"
s2_energy = 43
s3_name = "ISS Nova"
s3_energy = 96
s4_name = "ISS Pulsar"
s4_energy = 61
s5_name = "ISS Quasar"
s5_energy = 78
s6_name = "ISS Nebula"
s6_energy = 34
s7_name = "ISS Comet"
s7_energy = 55
s8_name = "ISS Vortex"
s8_energy = 92

# Step 2 – Status protocol
print("=== DOCK PROTOCOL ===")
print(f"{s1_name}: Energy {s1_energy}%")
print(f"{s2_name}: Energy {s2_energy}%")
print(f"{s3_name}: Energy {s3_energy}%")
print(f"{s4_name}: Energy {s4_energy}%")
print(f"{s5_name}: Energy {s5_energy}%")
print(f"{s6_name}: Energy {s6_energy}%")
print(f"{s7_name}: Energy {s7_energy}%")
print(f"{s8_name}: Energy {s8_energy}%")
print()

# Step 3 – Average
total_energy = s1_energy + s2_energy + s3_energy + s4_energy + s5_energy + s6_energy + s7_energy + s8_energy
average = total_energy / 8
print(f"Average energy: {average}%")

# Step 4 – Best ship
print(f"Best ship: {s3_name} with {s3_energy}% energy")

# Step 5 – Energy requirement
num_ships = 8
total_requirement = num_ships * 100
print(f"Total energy requirement (100% per ship): {total_requirement} units")

# Bonus
below_average = 0
if s1_energy < average: below_average += 1
if s2_energy < average: below_average += 1
if s3_energy < average: below_average += 1
if s4_energy < average: below_average += 1
if s5_energy < average: below_average += 1
if s6_energy < average: below_average += 1
if s7_energy < average: below_average += 1
if s8_energy < average: below_average += 1
print(f"Ships below average: {below_average}")
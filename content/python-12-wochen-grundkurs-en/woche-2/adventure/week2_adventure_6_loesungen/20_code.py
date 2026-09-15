# Step 1 - Create spells
s1_name = "Phoenix Fire"
s1_power = 92.5
s1_complexity = 5
s1_duration = 8

s2_name = "Frost Breath"
s2_power = 68.0
s2_complexity = 3
s2_duration = 4

s3_name = "Thunder Call"
s3_power = 75.5
s3_complexity = 4
s3_duration = 6

s4_name = "Light Shard"
s4_power = 55.0
s4_complexity = 2
s4_duration = 3

s5_name = "Shadow Wave"
s5_power = 83.0
s5_complexity = 4
s5_duration = 7

# Step 2 - Print descriptions
print("=== SPELL WORKSHOP LOG ===")
print(f"{s1_name}: Power {s1_power}, Complexity {s1_complexity}, Duration {s1_duration}s")
print(f"{s2_name}: Power {s2_power}, Complexity {s2_complexity}, Duration {s2_duration}s")
print(f"{s3_name}: Power {s3_power}, Complexity {s3_complexity}, Duration {s3_duration}s")
print(f"{s4_name}: Power {s4_power}, Complexity {s4_complexity}, Duration {s4_duration}s")
print(f"{s5_name}: Power {s5_power}, Complexity {s5_complexity}, Duration {s5_duration}s")
print()

# Step 3 - Sum up complexity
total_complexity = s1_complexity + s2_complexity + s3_complexity + s4_complexity + s5_complexity
print(f"Total complexity: {total_complexity}")

# Step 4 - Strongest and most complex spells
print(f"Strongest spell: {s1_name} ({s1_power})")
print(f"Most complex spell: {s1_name} (complexity {s1_complexity})")

# Step 5 - Average power
total_power = s1_power + s2_power + s3_power + s4_power + s5_power
average_power = total_power / 5
print(f"Average power: {average_power}")

# Step 6 - Filter the mighty ones (boolean)
s1_above_average = s1_power > average_power
s2_above_average = s2_power > average_power
s3_above_average = s3_power > average_power
s4_above_average = s4_power > average_power
s5_above_average = s5_power > average_power
print(f"{s1_name} above average: {s1_above_average}")
print(f"{s2_name} above average: {s2_above_average}")
print(f"{s3_name} above average: {s3_above_average}")
print(f"{s4_name} above average: {s4_above_average}")
print(f"{s5_name} above average: {s5_above_average}")

# Bonus: efficiency
print()
print(f"Efficiency {s1_name}: {s1_power / s1_complexity:.2f}")
print(f"Efficiency {s2_name}: {s2_power / s2_complexity:.2f}")
print(f"Efficiency {s3_name}: {s3_power / s3_complexity:.2f}")
print(f"Efficiency {s4_name}: {s4_power / s4_complexity:.2f}")
print(f"Efficiency {s5_name}: {s5_power / s5_complexity:.2f}")

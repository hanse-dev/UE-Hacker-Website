# Step 1 – Create exercises (5)
e1_name = "Dressage Basics"
e1_intensity = 2.5
e1_duration = 20
e1_difficulty = 2

e2_name = "Jumping Course"
e2_intensity = 4.5
e2_duration = 30
e2_difficulty = 5

e3_name = "Cross-Country Ride"
e3_intensity = 3.8
e3_duration = 45
e3_difficulty = 4

e4_name = "Lungeing Session"
e4_intensity = 2.0
e4_duration = 25
e4_difficulty = 2

e5_name = "Obstacle Work"
e5_intensity = 3.5
e5_duration = 35
e5_difficulty = 4

# Step 2 – Exercise descriptions
print("=== TRAINING HALL PROTOCOL ===")
print(f"{e1_name}: Intensity {e1_intensity}, Duration {e1_duration} min, Difficulty {e1_difficulty}")
print(f"{e2_name}: Intensity {e2_intensity}, Duration {e2_duration} min, Difficulty {e2_difficulty}")
print(f"{e3_name}: Intensity {e3_intensity}, Duration {e3_duration} min, Difficulty {e3_difficulty}")
print(f"{e4_name}: Intensity {e4_intensity}, Duration {e4_duration} min, Difficulty {e4_difficulty}")
print(f"{e5_name}: Intensity {e5_intensity}, Duration {e5_duration} min, Difficulty {e5_difficulty}")
print()

# Step 3 – Total duration
total_duration = e1_duration + e2_duration + e3_duration + e4_duration + e5_duration
print(f"Total duration: {total_duration} minutes")

# Step 4 – Most intense and difficult
print(f"Most intense exercise: {e2_name} ({e2_intensity})")
print(f"Most difficult exercise: {e2_name} (difficulty {e2_difficulty})")

# Step 5 – Average intensity
total_intensity = e1_intensity + e2_intensity + e3_intensity + e4_intensity + e5_intensity
average = total_intensity / 5
print(f"Average intensity: {average}")

# Step 6 – Boolean marking
e1_demanding = e1_intensity > average
e2_demanding = e2_intensity > average
e3_demanding = e3_intensity > average
e4_demanding = e4_intensity > average
e5_demanding = e5_intensity > average
print(f"{e1_name} above average: {e1_demanding}")
print(f"{e2_name} above average: {e2_demanding}")
print(f"{e3_name} above average: {e3_demanding}")
print(f"{e4_name} above average: {e4_demanding}")
print(f"{e5_name} above average: {e5_demanding}")

# Bonus: efficiency
print()
print(f"Efficiency {e1_name}: {e1_intensity / e1_duration * 10:.2f}")
print(f"Efficiency {e2_name}: {e2_intensity / e2_duration * 10:.2f}")
print(f"Efficiency {e3_name}: {e3_intensity / e3_duration * 10:.2f}")
print(f"Efficiency {e4_name}: {e4_intensity / e4_duration * 10:.2f}")
print(f"Efficiency {e5_name}: {e5_intensity / e5_duration * 10:.2f}")
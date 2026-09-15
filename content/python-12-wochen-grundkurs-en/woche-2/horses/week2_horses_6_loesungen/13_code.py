# Step 1 – Name the horses
horse1 = "Storm"
horse2 = "Sunshine"
horse3 = "Lightning"
ride_time1 = 45
ride_time2 = 30
ride_time3 = 60
difficulty1 = "easy"
difficulty2 = "medium"
difficulty3 = "advanced"

# Step 2 – Output lesson plan
print("=== RIDING LESSON PLAN ===")
print(f"{horse1}: {ride_time1} minutes, Difficulty: {difficulty1}")
print(f"{horse2}: {ride_time2} minutes, Difficulty: {difficulty2}")
print(f"{horse3}: {ride_time3} minutes, Difficulty: {difficulty3}")
print()

# Step 3 – Total time
total_time = ride_time1 + ride_time2 + ride_time3
print(f"Total riding time: {total_time} minutes")

# Step 4 – Average time
average = total_time / 3
print(f"Average time: {average} minutes")
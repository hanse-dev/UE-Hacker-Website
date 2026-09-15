# Step 1: Exercise list
exercises = ["Dressage", "Show Jumping", "Canter", "Trot", "Walk"]
print(exercises)
print(f"Number of exercises: {len(exercises)}")

# Step 2: Add and remove
exercises.append("Vaulting")
exercises.insert(0, "Warm-Up")
completed = exercises.pop()
print(f"Completed: {completed}")
print(exercises)

# Step 3: Search and sort
exercises.sort()
print(f"Sorted: {exercises}")
print(f"'Canter' is at index: {exercises.index('Canter')}")
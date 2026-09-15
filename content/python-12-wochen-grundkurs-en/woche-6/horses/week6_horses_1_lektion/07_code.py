# 🔍 Exercises with append() and insert()

# Example 1: Adding elements
training_plan = []
print(f"Empty training plan: {training_plan}")

# Add at the end with append()
training_plan.append("Lungeing")
print(f"After append: {training_plan}")

training_plan.append("Dressage")
training_plan.append("Show Jumping")
print(f"Fully filled: {training_plan}")

# Insert at a specific position with insert()
training_plan.insert(0, "Warm-Up")  # At the beginning
print(f"After insert(0): {training_plan}")

training_plan.insert(2, "Cavaletti")  # At position 2
print(f"After insert(2): {training_plan}")
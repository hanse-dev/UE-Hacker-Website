# Example 2: Capsules are immutable
training_status = ("Active", "Stable", "Healthy")
print(f"Training status: {training_status}")

# Access works
print(f"Status: {training_status[0]}")

# Changing does NOT work!
try:
    training_status[0] = "Inactive"
except TypeError as e:
    print(f"Error: {e}")

# But capsules inside lists can be replaced
training = [
    ("Dressage", "Active"),
    ("Jumping", "Stable"),
    ("Western", "Healthy")
]
training[1] = ("Jumping", "Inactive")
print(f"\nTraining after change: {training}")
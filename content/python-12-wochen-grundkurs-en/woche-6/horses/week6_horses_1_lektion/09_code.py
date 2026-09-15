# Example 3: Combining lists
horses = ["Thunder", "Luna", "Storm"]
riders = ["Anna", "Max", "Sarah"]
trainings = ["Dressage", "Show Jumping", "Western"]

print("=== Combining Lists ===")
print(f"Horses: {horses}")
print(f"Riders: {riders}")
print(f"Trainings: {trainings}")

# Combine with + operator
all_together = horses + riders + trainings
print(f"All combined: {all_together}")

# Add one list to another with extend()
horses.extend(riders)
print(f"Horses extended: {horses}")
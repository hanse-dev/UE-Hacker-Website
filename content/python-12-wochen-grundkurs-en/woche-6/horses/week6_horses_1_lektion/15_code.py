horses = ["Thunder", "Luna", "Storm", "Shadow", "Bella"]

# break: stop searching once the horse is found
print("=== Horse Search ===")
for horse in horses:
    print(f"Checking: {horse}")
    if horse == "Storm":
        print("🐎 Storm found! Search stopped.")
        break

# continue: skip sick horses during training
print("\n=== Training Plan Without Sick Horses ===")
sick_horses = ["Luna"]
for horse in horses:
    if horse in sick_horses:
        continue
    print(f"  - {horse} is being trained")
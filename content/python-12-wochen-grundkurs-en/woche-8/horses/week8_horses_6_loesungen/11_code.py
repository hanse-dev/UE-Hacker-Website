# Step 1: Create a horse stable card
horse = {
    "name": "Thunder",
    "breed": "Hanoverian",
    "age": 7,
    "height": 168  # height at withers in cm
}
print("Horse stable card:")
print(horse)

# Step 2: Change and extend values
horse["age"] = 8
horse["owner"] = "Lena Miller"
print(f"\nAfter update: Age {horse['age']}, Owner {horse['owner']}")

# Step 3: List of horse dictionaries
horse_list = [
    {"name": "Thunder", "breed": "Hanoverian", "age": 8},
    {"name": "Luna", "breed": "Icelandic", "age": 5},
    {"name": "Flash", "breed": "Arabian", "age": 4}
]
print(f"\nHorse list: {horse_list}")
print(f"First horse: {horse_list[0]['name']}")

# Step 4: Access and output
h_name = horse["name"]
h_breed = horse.get("breed")
print(f"\nHorse: {h_name}, Breed: {h_breed}, Age: {horse['age']}")

# Bonus: Nested dictionary
horse["health"] = {"vaccination": "current", "hoof": "well-maintained", "dentist": "2025"}
print(f"Hoof status: {horse['health']['hoof']}")
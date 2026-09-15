import json

# Step 1: Horse data as dictionary
horse = {
    'name': 'Luna',
    'breed': 'Andalusian',
    'age': 7,
    'owner': 'Maria Schneider'
}
print('Horse data:', horse)

# Step 2: JSON export
with open('horse.json', 'w') as f:
    json.dump(horse, f, indent=2)
print('Horse saved to horse.json!')

# Step 3: JSON import
with open('horse.json', 'r') as f:
    loaded_data = json.load(f)

print(f'Loaded horse: {loaded_data["name"]}')
print('All data:', loaded_data)

# Step 4: Statistics
print(f'\n=== Horse Profile ===')
print(f'Name: {loaded_data["name"]}')
print(f'Breed: {loaded_data["breed"]}')
print(f'Age: {loaded_data["age"]} years')
print(f'Owner: {loaded_data["owner"]}')
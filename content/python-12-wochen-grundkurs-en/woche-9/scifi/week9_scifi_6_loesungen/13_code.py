import json

# Step 1: Ship data as dictionary
ship = {
    'name': 'Nebula-7',
    'type_': 'Exploration Cruiser',
    'crew': 42,
    'systems': ['Life Support', 'Propulsion', 'Weapons', 'Sensors']
}
print('Ship data:', ship)

# Step 2: JSON export
with open('ship.json', 'w') as f:
    json.dump(ship, f, indent=2)
print('Ship data saved to ship.json!')

# Step 3: JSON import
with open('ship.json', 'r') as f:
    loaded_data = json.load(f)

print(f'Loaded ship: {loaded_data["name"]}')
print('All data:', loaded_data)

# Step 4: Statistics
print(f'\n=== Ship Statistics ===')
print(f'Name: {loaded_data["name"]}')
print(f'Type: {loaded_data["type_"]}')
print(f'Crew strength: {loaded_data["crew"]} persons')
print(f'Active systems: {len(loaded_data["systems"])}')
for system in loaded_data['systems']:
    print(f'  - {system}')
import json

# Step 1: Create treasure map
treasure_map = {
    'Dragon Cave': {'coordinates': [42, 17], 'value': 1500, 'description': 'Deep in the mountains'},
    'Sunken Temple': {'coordinates': [88, 55], 'value': 3200, 'description': 'Beneath the ancient lake'},
    'Goblin Fortress': {'coordinates': [23, 91], 'value': 800, 'description': 'In the dark forest'},
}

with open('treasure_map.json', 'w') as f:
    json.dump(treasure_map, f, indent=2)

print('Treasure map saved!')

# Step 2: Load and display map
with open('treasure_map.json', 'r') as f:
    loaded_map = json.load(f)

print('\n=== Treasure Map ===')
for location, info in loaded_map.items():
    print(f'  Location: {location}')
    print(f'    Coordinates: {info["coordinates"]}')
    print(f'    Value: {info["value"]} Gold')
    print(f'    Description: {info["description"]}')

# Step 3: Add new entry
loaded_map['Elven Forest Glade'] = {
    'coordinates': [66, 33],
    'value': 2100,
    'description': 'Hidden in the Silver Elven Forest'
}

with open('treasure_map.json', 'w') as f:
    json.dump(loaded_map, f, indent=2)

print('\n=== Updated Treasure Map ===')
for location, info in loaded_map.items():
    print(f'  {location}: {info["value"]} Gold')

# Bonus: find most valuable treasure
most_valuable = max(loaded_map, key=lambda loc: loaded_map[loc]['value'])
print(f'\n*** Most Valuable Treasure: {most_valuable} ({loaded_map[most_valuable]["value"]} Gold) ***')
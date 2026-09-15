import json

# Step 1: Hero data as dictionary
hero = {
    'name': 'Thorin Oakenshield',
    'hero_class': 'Warrior',
    'level': 12,
    'hit_points': 250
}
print('Hero data:', hero)

# Step 2: JSON export
with open('hero.json', 'w') as f:
    json.dump(hero, f, indent=2)
print('Hero saved to hero.json!')

# Step 3: JSON import
with open('hero.json', 'r') as f:
    loaded_data = json.load(f)

print(f'Loaded hero: {loaded_data["name"]}')
print('All data:', loaded_data)

# Step 4: Statistics
print(f'\n=== Hero Statistics ===')
print(f'Name: {loaded_data["name"]}')
print(f'Class: {loaded_data["hero_class"]}')
print(f'Level: {loaded_data["level"]}')
print(f'Hit Points: {loaded_data["hit_points"]}')
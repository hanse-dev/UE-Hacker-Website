import json

# Step 1: Create stable card
stable_card = {
    'Luna': {'breed': 'Andalusian', 'stall': 3, 'feed_ration': 6.5},
    'Spirit': {'breed': 'Icelandic', 'stall': 7, 'feed_ration': 5.0},
    'Rocco': {'breed': 'Icelandic', 'stall': 1, 'feed_ration': 4.5},
}

with open('stable_card.json', 'w') as f:
    json.dump(stable_card, f, indent=2)

print('Stable card saved!')

# Step 2: Load and display card
with open('stable_card.json', 'r') as f:
    loaded_card = json.load(f)

print('\n=== Stable Card ===')
for name, info in loaded_card.items():
    print(f'  Horse: {name}')
    print(f'    Breed: {info["breed"]}')
    print(f'    Stall: {info["stall"]}')
    print(f'    Feed ration: {info["feed_ration"]} kg/day')

# Step 3: Add new horse
loaded_card['Bella'] = {
    'breed': 'Shetland Pony',
    'stall': 12,
    'feed_ration': 3.0
}

with open('stable_card.json', 'w') as f:
    json.dump(loaded_card, f, indent=2)

print('\n=== Updated Stable Card ===')
for name, info in loaded_card.items():
    print(f'  {name} (Stall {info["stall"]}): {info["feed_ration"]} kg feed/day')

# Bonus: calculate total feed ration
total_feed = sum(info['feed_ration'] for info in loaded_card.values())
print(f'\nTotal feed ration per day: {total_feed:.1f} kg')
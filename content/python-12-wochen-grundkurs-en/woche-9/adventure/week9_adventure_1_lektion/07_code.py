# 🔍 Exercises with JSON
import json

# Example 1: Dictionary to JSON
hero = {
    'name': 'Aria',
    'class': 'Mage',
    'level': 15,
    'abilities': ['Fireball', 'Heal', 'Shield']
}

# Convert to JSON string
json_string = json.dumps(hero, indent=2)
print('=== JSON String ===')
print(json_string)

# Back to dictionary
back = json.loads(json_string)
print(f'\nName: {back["name"]}')

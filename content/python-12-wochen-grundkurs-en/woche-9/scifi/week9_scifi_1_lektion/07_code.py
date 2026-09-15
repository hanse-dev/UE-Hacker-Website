# 🔍 Exercises with JSON
import json

# Example 1: Dictionary to JSON
ship = {
    'name': 'Nebula-Explorer',
    'type': 'Research',
    'crew': 150,
    'systems': ['Propulsion', 'Life Support', 'Communications']
}

# Convert to JSON string
json_string = json.dumps(ship, indent=2)
print('=== JSON String ===')
print(json_string)

# Convert back to dictionary
back = json.loads(json_string)
print(f'\nName: {back["name"]}')

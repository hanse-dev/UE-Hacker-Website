# 🔍 Exercises with JSON
import json

# Example 1: Dictionary to JSON
horse = {
    'name': 'Thunder',
    'breed': 'Hanoverian',
    'age': 8,
    'height': 1.72,
    'skills': ['Dressage', 'Jumping', 'Western']
}

# Convert to JSON string
json_string = json.dumps(horse, indent=2)
print('=== JSON String ===')
print(json_string)

# Back to dictionary
back = json.loads(json_string)
print(f'\nName: {back["name"]}')
# Example 3: Complex data structures with JSON
stable = {
    'name': 'Sunny Valley',
    'location': {
        'region': 'Southern Germany',
        'coordinates': [100, 200]
    },
    'horses': [
        {'name': 'Thunder', 'breed': 'Hanoverian'},
        {'name': 'Luna', 'breed': 'Icelandic'}
    ],
    'status': 'Active'
}

# Save
with open('stable_data.json', 'w') as f:
    json.dump(stable, f, indent=2)

# Load and analyse
with open('stable_data.json', 'r') as f:
    stable_data = json.load(f)

print(f'Stable: {stable_data["name"]}')
print(f'Region: {stable_data["location"]["region"]}')
print(f'Horses: {len(stable_data["horses"])}')
print(f'Status: {stable_data["status"]}')
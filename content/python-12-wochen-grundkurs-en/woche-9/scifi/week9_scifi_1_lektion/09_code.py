# Example 3: Complex data structures with JSON
space_station = {
    'name': 'Nebula-7',
    'position': {
        'sector': 'Alpha',
        'coordinates': [100, 200, 300]
    },
    'crew': [
        {'name': 'Alex', 'role': 'Commander'},
        {'name': 'Zara', 'role': 'Scientist'}
    ],
    'status': 'Online'
}

# Save
with open('space_station.json', 'w') as f:
    json.dump(space_station, f, indent=2)

# Load and analyse
with open('space_station.json', 'r') as f:
    station = json.load(f)

print(f'Station: {station["name"]}')
print(f'Sector: {station["position"]["sector"]}')
print(f'Crew size: {len(station["crew"])}')
print(f'Status: {station["status"]}')

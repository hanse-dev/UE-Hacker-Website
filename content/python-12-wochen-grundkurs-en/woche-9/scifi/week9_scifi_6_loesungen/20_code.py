import json

star_map = {
    'Alpha Centauri': {'coordinates': [4.37, 0.0, 0.0], 'status': 'Explored', 'distance_ly': 4.37},
    'Proxima Centauri': {'coordinates': [4.24, 0.1, 0.3], 'status': 'Explored', 'distance_ly': 4.24},
    'Tau Ceti': {'coordinates': [11.9, 2.1, -1.5], 'status': 'Unknown', 'distance_ly': 11.9},
}

with open('star_map.json', 'w') as f:
    json.dump(star_map, f, indent=2)

print('Star map saved!')

with open('star_map.json', 'r') as f:
    loaded_map = json.load(f)

print('\n=== Star Map ===')
for name, info in loaded_map.items():
    print(f'  System: {name}')
    print(f'    Coordinates: {info["coordinates"]}')
    print(f'    Status: {info["status"]}')
    print(f'    Distance: {info["distance_ly"]} light years')

loaded_map['Kepler-452'] = {
    'coordinates': [1400.0, 55.2, -12.7],
    'status': 'Unknown',
    'distance_ly': 1400.0
}

with open('star_map.json', 'w') as f:
    json.dump(loaded_map, f, indent=2)

print('\n=== Updated Star Map ===')
for name, info in loaded_map.items():
    print(f'  {name}: {info["distance_ly"]} light years – {info["status"]}')

most_distant = max(loaded_map, key=lambda s: loaded_map[s]['distance_ly'])
print(f'\n*** Most Distant System: {most_distant} ({loaded_map[most_distant]["distance_ly"]} light years) ***')
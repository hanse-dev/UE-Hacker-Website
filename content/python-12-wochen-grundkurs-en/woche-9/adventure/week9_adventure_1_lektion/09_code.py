# Example 3: Complex data structures with JSON
guild = {
    'name': 'Heroes of Pyralia',
    'location': {
        'region': 'Central Pyralia',
        'coordinates': [100, 200]
    },
    'members': [
        {'name': 'Aria', 'role': 'Mage'},
        {'name': 'Thorin', 'role': 'Warrior'}
    ],
    'status': 'Active'
}

# Save
with open('guild_data.json', 'w') as f:
    json.dump(guild, f, indent=2)

# Load and analyse
with open('guild_data.json', 'r') as f:
    guild_data = json.load(f)

print(f'Guild: {guild_data["name"]}')
print(f'Region: {guild_data["location"]["region"]}')
print(f'Members: {len(guild_data["members"])}')
print(f'Status: {guild_data["status"]}')

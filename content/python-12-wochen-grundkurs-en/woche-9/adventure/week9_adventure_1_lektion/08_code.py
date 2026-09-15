# Example 2: Write and read JSON scrolls
# Save to scroll
with open('hero_data.json', 'w') as f:
    json.dump(hero, f, indent=2)

print('✅ Hero data saved!')

# Load from scroll
with open('hero_data.json', 'r') as f:
    loaded = json.load(f)

print('=== Loaded Data ===')
print(f'Hero: {loaded["name"]}')
print(f'Abilities: {", ".join(loaded["abilities"])}')

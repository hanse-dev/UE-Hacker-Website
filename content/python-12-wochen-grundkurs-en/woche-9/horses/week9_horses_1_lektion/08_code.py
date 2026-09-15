# Example 2: Write and read JSON files
# Save to file
with open('horse_data.json', 'w') as f:
    json.dump(horse, f, indent=2)

print('✅ Horse data saved!')

# Load from file
with open('horse_data.json', 'r') as f:
    loaded = json.load(f)

print('=== Loaded Data ===')
print(f'Horse: {loaded["name"]}')
print(f'Skills: {", ".join(loaded["skills"])}')
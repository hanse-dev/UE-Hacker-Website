# Example 2: Writing and reading JSON files
# Save to file
with open('ship_data.json', 'w') as f:
    json.dump(ship, f, indent=2)

print('✅ Ship data saved!')

# Load from file
with open('ship_data.json', 'r') as f:
    loaded = json.load(f)

print('=== Loaded Data ===')
print(f'Ship: {loaded["name"]}')
print(f'Systems: {", ".join(loaded["systems"])}')

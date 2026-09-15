# Example 1: Write CSV scrolls
import csv

# Hero data
hero_data = [
    ['Name', 'Class', 'Level', 'Experience'],
    ['Aria', 'Mage', 15, 2500],
    ['Thorin', 'Warrior', 18, 3200],
    ['Luna', 'Rogue', 12, 1800]
]

# Write CSV
with open('hero_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(hero_data)

print('✅ CSV scroll created!')

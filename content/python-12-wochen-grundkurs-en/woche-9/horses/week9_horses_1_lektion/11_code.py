# Example 1: Write CSV files
import csv

# Horse data
horse_data = [
    ['Name', 'Breed', 'Age', 'Height', 'Owner'],
    ['Thunder', 'Hanoverian', 8, 1.72, 'Anna'],
    ['Luna', 'Icelandic', 6, 1.35, 'Tom'],
    ['Stormy', 'Quarter Horse', 10, 1.58, 'Maria']
]

# Write CSV
with open('horse_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(horse_data)

print('✅ CSV file created!')
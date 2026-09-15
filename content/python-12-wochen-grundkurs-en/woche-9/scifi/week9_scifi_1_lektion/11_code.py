# Example 1: Writing CSV files
import csv

# Crew data
crew_data = [
    ['Name', 'Role', 'Age', 'Experience'],
    ['Captain Alex', 'Commander', 35, 15],
    ['Dr. Zara', 'Scientist', 28, 8],
    ['Lt. Nova', 'Pilot', 26, 6]
]

# Write CSV
with open('crew_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(crew_data)

print('✅ CSV file created!')

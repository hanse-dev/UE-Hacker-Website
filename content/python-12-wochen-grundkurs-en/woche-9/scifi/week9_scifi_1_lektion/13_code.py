# Example 3: CSV with DictReader/DictWriter
# Write with DictWriter
fields = ['name', 'role', 'age', 'experience']

with open('crew_data_dict.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    writer.writerow({'name': 'Captain Alex', 'role': 'Commander', 'age': 35, 'experience': 15})
    writer.writerow({'name': 'Dr. Zara', 'role': 'Scientist', 'age': 28, 'experience': 8})

# Read with DictReader
with open('crew_data_dict.csv', 'r') as f:
    reader = csv.DictReader(f)

    print('=== Crew Statistics ===')
    for row in reader:
        print(f'{row["name"]} ({row["role"]}): {row["age"]} years')

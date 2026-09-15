# Example 3: CSV with DictReader/DictWriter
# Write with DictWriter
fields = ['name', 'class', 'level', 'experience']

with open('hero_data_dict.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    writer.writerow({'name': 'Aria', 'class': 'Mage', 'level': 15, 'experience': 2500})
    writer.writerow({'name': 'Thorin', 'class': 'Warrior', 'level': 18, 'experience': 3200})

# Read with DictReader
with open('hero_data_dict.csv', 'r') as f:
    reader = csv.DictReader(f)

    print('=== Hero Statistics ===')
    for row in reader:
        print(f'{row["name"]} ({row["class"]}): Level {row["level"]}')

# Example 3: CSV with DictReader/DictWriter
# Write with DictWriter
fields = ['name', 'breed', 'age', 'height', 'owner']

with open('horse_data_dict.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    
    writer.writerow({'name': 'Thunder', 'breed': 'Hanoverian', 'age': 8, 'height': 1.72, 'owner': 'Anna'})
    writer.writerow({'name': 'Luna', 'breed': 'Icelandic', 'age': 6, 'height': 1.35, 'owner': 'Tom'})

# Read with DictReader
with open('horse_data_dict.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    print('=== Horse Statistics ===')
    for row in reader:
        print(f'{row["name"]} ({row["breed"]}): {row["age"]} years, {row["height"]}m')
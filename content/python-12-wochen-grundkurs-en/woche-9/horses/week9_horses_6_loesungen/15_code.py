import csv

# Step 1: CSV export
horses = [
    {'name': 'Luna', 'breed': 'Andalusian', 'age': '7'},
    {'name': 'Spirit', 'breed': 'Icelandic', 'age': '12'},
    {'name': 'Rocco', 'breed': 'Icelandic', 'age': '5'},
    {'name': 'Bella', 'breed': 'Shetland Pony', 'age': '9'},
    {'name': 'Thunder', 'breed': 'Andalusian', 'age': '4'},
]

with open('horses.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'breed', 'age'])
    writer.writeheader()
    writer.writerows(horses)

print('Horses saved to horses.csv!')

# Step 2: CSV import
read_horses = []
with open('horses.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        read_horses.append(row)

print(f'Entries read: {len(read_horses)}')
print(f'First entry: {read_horses[0]}')

# Step 3: Search function by breed
def search_by_breed(filename, breed):
    results = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['breed'] == breed:
                results.append(row)
    return results

icelandics = search_by_breed('horses.csv', 'Icelandic')
print(f'\nIcelandic horses found:')
for h in icelandics:
    print(f'  {h["name"]} (Age: {h["age"]} years)')

# Step 4: Short report
total_age = sum(int(h['age']) for h in read_horses)
average = total_age / len(read_horses)

breed_count = {}
for h in read_horses:
    b = h['breed']
    breed_count[b] = breed_count.get(b, 0) + 1

print(f'\n=== Stable Report ===')
print(f'Average age: {average:.1f} years')
print('Count per breed:')
for breed, count in breed_count.items():
    print(f'  {breed}: {count}')
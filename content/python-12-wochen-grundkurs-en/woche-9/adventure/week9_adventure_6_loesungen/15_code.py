import csv

# Step 1: CSV export
heroes = [
    {'name': 'Lyra', 'hero_class': 'Archer', 'level': '8'},
    {'name': 'Gorund', 'hero_class': 'Warrior', 'level': '12'},
    {'name': 'Selene', 'hero_class': 'Mage', 'level': '10'},
    {'name': 'Finn', 'hero_class': 'Archer', 'level': '5'},
    {'name': 'Mira', 'hero_class': 'Mage', 'level': '7'},
]

with open('heroes.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'hero_class', 'level'])
    writer.writeheader()
    writer.writerows(heroes)

print('Heroes saved to heroes.csv!')

# Step 2: CSV import
read_heroes = []
with open('heroes.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        read_heroes.append(row)

print(f'Number of entries read: {len(read_heroes)}')
print(f'First entry: {read_heroes[0]}')

# Step 3: Search function
def search_by_class(filename, hero_class):
    results = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['hero_class'] == hero_class:
                results.append(row)
    return results

mages = search_by_class('heroes.csv', 'Mage')
print(f'\nMages found:')
for m in mages:
    print(f'  {m["name"]} (Level {m["level"]})')

# Step 4: Short report
total_level = sum(int(h['level']) for h in read_heroes)
average = total_level / len(read_heroes)

class_count = {}
for h in read_heroes:
    c = h['hero_class']
    class_count[c] = class_count.get(c, 0) + 1

print(f'\n=== Guild Report ===')
print(f'Average level: {average:.1f}')
print('Count per class:')
for cls, count in class_count.items():
    print(f'  {cls}: {count}')
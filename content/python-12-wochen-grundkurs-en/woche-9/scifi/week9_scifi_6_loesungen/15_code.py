import csv

# Step 1: CSV export
crew = [
    {'name': 'Commander Shepard', 'rank': 'Commander', 'age': '35'},
    {'name': 'Dr. Vasquez', 'rank': 'Doctor', 'age': '29'},
    {'name': 'Hicks', 'rank': 'Sergeant', 'age': '31'},
    {'name': 'Reyes', 'rank': 'Pilot', 'age': '27'},
    {'name': 'Chen', 'rank': 'Pilot', 'age': '33'},
]

with open('crew.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'rank', 'age'])
    writer.writeheader()
    writer.writerows(crew)

print('Crew data saved to crew.csv!')

# Step 2: CSV import
read_crew = []
with open('crew.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        read_crew.append(row)

print(f'Entries read: {len(read_crew)}')
print(f'First entry: {read_crew[0]}')

# Step 3: Search function by rank
def search_by_rank(filename, rank):
    results = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['rank'] == rank:
                results.append(row)
    return results

pilots = search_by_rank('crew.csv', 'Pilot')
print(f'\nPilots found:')
for p in pilots:
    print(f'  {p["name"]} (Age: {p["age"]})')

# Step 4: Short report
total_age = sum(int(m['age']) for m in read_crew)
average = total_age / len(read_crew)

rank_count = {}
for m in read_crew:
    r = m['rank']
    rank_count[r] = rank_count.get(r, 0) + 1

print(f'\n=== Crew Report ===')
print(f'Average age: {average:.1f} years')
print('Count per rank:')
for rank, count in rank_count.items():
    print(f'  {rank}: {count}')
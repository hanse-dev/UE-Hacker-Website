# Example 2: Read CSV files
with open('horse_data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    
    print('=== Horse Analysis ===')
    for row in reader:
        name, breed, age, height, owner = row
        print(f'{name}: {breed}, {age} years, {height}m, Owner: {owner}')
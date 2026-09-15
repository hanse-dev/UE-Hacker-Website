# Example 2: Reading CSV files
with open('crew_data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header

    print('=== Crew Analysis ===')
    for row in reader:
        name, role, age, experience = row
        print(f'{name}: {role}, {age} years, {experience} yrs experience')

# Example 2: Read CSV scrolls
with open('hero_data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header

    print('=== Hero Analysis ===')
    for row in reader:
        name, hero_class, level, experience = row
        print(f'{name}: {hero_class}, Level {level}, {experience} XP')

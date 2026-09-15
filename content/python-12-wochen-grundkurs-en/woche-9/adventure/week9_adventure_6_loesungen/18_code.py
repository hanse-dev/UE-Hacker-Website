# Boss Quest 1: The Hero's Diary
# Note: input() replaced with fixed example values

# Step 1: Write entry
date = '2024-06-17'
entry = 'Defeated the Goblin Captain in the Cave of Forgetting'

with open('hero_diary.txt', 'w') as f:
    f.write(f'[{date}] {entry}\n')

print('Entry saved!')

# Step 2: Read diary
with open('hero_diary.txt', 'r') as f:
    print('\n=== Hero Diary ===')
    print(f.read())

# Step 3: Append 3 more entries
more_entries = [
    ('2024-06-18', 'Found the Magic Bag in the ancient temple'),
    ('2024-06-19', 'Saved the village from the Walking Bone Mountain'),
    ('2024-06-20', 'Received the Guild Master Certificate from the Council of Sages'),
]

with open('hero_diary.txt', 'a') as f:
    for d, e in more_entries:
        f.write(f'[{d}] {e}\n')

# Print full diary
with open('hero_diary.txt', 'r') as f:
    lines = f.readlines()

print('=== Full Diary ===')
for line in lines:
    print(line.strip())

# Bonus: count entries
print(f'\nTotal entries: {len(lines)}')
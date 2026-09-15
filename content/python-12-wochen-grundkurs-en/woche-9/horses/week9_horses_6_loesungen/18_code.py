# Boss Quest 1: The Training Diary
# Note: input() replaced with fixed example values

# Step 1: Write training entry
date = '2024-06-17'
horse_name = 'Luna'
exercise = 'Trot exercises on the outdoor arena – 30 minutes'

with open('training_diary.txt', 'w') as f:
    f.write(f'[{date}] Horse: {horse_name} | Exercise: {exercise}\n')

print('Training entry saved!')

# Step 2: Read diary
with open('training_diary.txt', 'r') as f:
    print('\n=== Training Diary ===')
    print(f.read())

# Step 3: Append 3 more entries
more_entries = [
    ('2024-06-18', 'Spirit', 'Canter work in the countryside – 45 minutes'),
    ('2024-06-19', 'Luna', 'Jumping training – 1 hour'),
    ('2024-06-20', 'Rocco', 'Lungeing for warm-up – 20 minutes'),
]

with open('training_diary.txt', 'a') as f:
    for d, h, e in more_entries:
        f.write(f'[{d}] Horse: {h} | Exercise: {e}\n')

# Print full diary
with open('training_diary.txt', 'r') as f:
    lines = f.readlines()

print('=== Full Training Diary ===')
for line in lines:
    print(line.strip())

# Bonus: count training sessions
print(f'\nTotal training sessions: {len(lines)}')
from datetime import datetime

# Step 1: Write quest log
with open('quest_log.txt', 'w') as f:
    f.write('[INFO] Quest started: Defeat the Dragon\n')
    f.write('[INFO] Hero enters the Dragon Cave\n')
    f.write('[WARN] Health below 50 XP\n')

print('Quest log created!')

# Step 2: Add timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
new_entry = f'[INFO] {timestamp} - Hero drinks healing potion\n'

with open('quest_log.txt', 'a') as f:
    f.write(new_entry)

print(f'New entry: {new_entry.strip()}')

# Step 3: Log level — read and print full file
with open('quest_log.txt', 'r') as f:
    content = f.read()

print('\n=== Quest Log ===')
print(content)

# Step 4: Filter function
def filter_level(filename, level):
    results = []
    with open(filename, 'r') as f:
        for line in f:
            if f'[{level}]' in line:
                results.append(line.strip())
    return results

warn_entries = filter_level('quest_log.txt', 'WARN')
print('=== WARN entries only ===')
for entry in warn_entries:
    print(entry)
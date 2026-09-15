from datetime import datetime

# Step 1: Write log file
with open('log.txt', 'w') as f:
    f.write('[INFO] Space Station Nebula-7 started\n')
    f.write('[INFO] All systems nominal\n')
    f.write('[WARN] Oxygen level on Deck 3 slightly elevated\n')

print('Log file created!')

# Step 2: Add timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
new_entry = f'[INFO] {timestamp} - Hyperdrive activated\n'

with open('log.txt', 'a') as f:
    f.write(new_entry)

print(f'New entry: {new_entry.strip()}')

# Step 3: Read and print full log
with open('log.txt', 'r') as f:
    content = f.read()

print('\n=== System Log ===')
print(content)

# Step 4: Filter function
def filter_level(filename, level):
    results = []
    with open(filename, 'r') as f:
        for line in f:
            if f'[{level}]' in line:
                results.append(line.strip())
    return results

warn_entries = filter_level('log.txt', 'WARN')
print('=== WARN entries only ===')
for entry in warn_entries:
    print(entry)
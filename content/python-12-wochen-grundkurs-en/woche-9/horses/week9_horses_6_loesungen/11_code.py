from datetime import datetime

# Step 1: Write stable log
with open('stable_log.txt', 'w') as f:
    f.write('[INFO] Luna: Morning feeding complete\n')
    f.write('[INFO] Spirit: Hooves cleaned\n')
    f.write('[WARN] Rocco: Hoof injury detected – notify vet\n')

print('Stable log created!')

# Step 2: Add timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
new_entry = f'[INFO] {timestamp} - Luna: Evening training completed\n'

with open('stable_log.txt', 'a') as f:
    f.write(new_entry)

print(f'New entry: {new_entry.strip()}')

# Step 3: Read and print full log
with open('stable_log.txt', 'r') as f:
    content = f.read()

print('\n=== Stable Log ===')
print(content)

# Step 4: Filter function
def filter_level(filename, level):
    results = []
    with open(filename, 'r') as f:
        for line in f:
            if f'[{level}]' in line:
                results.append(line.strip())
    return results

warn_entries = filter_level('stable_log.txt', 'WARN')
print('=== WARN entries only ===')
for entry in warn_entries:
    print(entry)
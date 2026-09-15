# Example 3: Appending to files and error handling
# Append to an existing file
with open('mission_log.txt', 'a') as f:
    f.write('Update: Systems nominal\n')

print('✅ Update added!')

# With error handling
try:
    with open('does_not_exist.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('❌ File not found!')

# Check if file exists
import os
if os.path.exists('mission_log.txt'):
    print('✅ Mission log exists!')
else:
    print('❌ Mission log not found!')

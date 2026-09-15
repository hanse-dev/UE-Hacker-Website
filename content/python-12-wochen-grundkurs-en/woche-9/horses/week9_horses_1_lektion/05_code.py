# Example 3: Appending to files and error handling
# Append to an existing file
with open('horses_log.txt', 'a') as f:
    f.write('Update: Feed delivery arrived\n')

print('✅ Update added!')

# With error handling
try:
    with open('does_not_exist.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('❌ File not found!')

# Check if file exists
import os
if os.path.exists('horses_log.txt'):
    print('✅ Horse log exists!')
else:
    print('❌ Horse log not found!')
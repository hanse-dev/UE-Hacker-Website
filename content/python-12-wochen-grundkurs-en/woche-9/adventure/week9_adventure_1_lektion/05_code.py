# Example 3: Appending to scrolls and error handling
# Append to existing scroll
with open('quest_log.txt', 'a') as f:
    f.write('Update: Monster defeated\n')

print('✅ Update added!')

# With error handling
try:
    with open('does_not_exist.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('❌ Scroll not found!')

# Check if scroll exists
import os
if os.path.exists('quest_log.txt'):
    print('✅ Quest log exists!')
else:
    print('❌ Quest log not found!')

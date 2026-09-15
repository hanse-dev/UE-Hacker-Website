# Example 1: Simple file operations
# Write a file
with open('horses_log.txt', 'w') as f:
    f.write('Sunny Valley Horse Log\n')
    f.write('Date: 15.03.2025\n')
    f.write('Status: All horses healthy\n')

print('✅ Horse log created!')

# Read the file
with open('horses_log.txt', 'r') as f:
    content = f.read()
    print('=== Horse Log ===')
    print(content)
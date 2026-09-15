# Example 1: Simple file operations
# Write file
with open('mission_log.txt', 'w') as f:
    f.write('Nebula-7 Mission Log\n')
    f.write('Date: 2157.03.15\n')
    f.write('Status: Active\n')

print('✅ Mission log created!')

# Read file
with open('mission_log.txt', 'r') as f:
    content = f.read()
    print('=== Mission Log ===')
    print(content)

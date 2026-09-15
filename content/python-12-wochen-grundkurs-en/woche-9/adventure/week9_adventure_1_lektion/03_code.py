# Example 1: Simple scroll operations
# Write scroll
with open('quest_log.txt', 'w') as f:
    f.write('Pyralia Quest Log\n')
    f.write('Date: March 15, 1257\n')
    f.write('Status: Active\n')

print('✅ Quest log created!')

# Read scroll
with open('quest_log.txt', 'r') as f:
    content = f.read()
    print('=== Quest Log ===')
    print(content)

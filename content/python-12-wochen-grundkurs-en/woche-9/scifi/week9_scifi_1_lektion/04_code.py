# Example 2: Line-by-line access
# Save multiple entries
crew_data = [
    'Captain Alex,35,15\n',
    'Dr. Zara,28,8\n',
    'Lt. Nova,26,6\n'
]

with open('crew_list.txt', 'w') as f:
    f.writelines(crew_data)

print('✅ Crew list saved!')

# Read line by line
with open('crew_list.txt', 'r') as f:
    print('=== Crew Members ===')
    for line in f:
        data = line.strip().split(',')
        print(f'Name: {data[0]}, Age: {data[1]}, Experience: {data[2]}')

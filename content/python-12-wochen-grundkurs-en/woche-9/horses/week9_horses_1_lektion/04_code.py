# Example 2: Line-by-line access
# Save multiple entries
horse_data = [
    'Thunder,Hanoverian,8,1.72\n',
    'Luna,Icelandic,6,1.35\n',
    'Stormy,Quarter Horse,10,1.58\n'
]

with open('horses_list.txt', 'w') as f:
    f.writelines(horse_data)

print('✅ Horse list saved!')

# Read line by line
with open('horses_list.txt', 'r') as f:
    print('=== Horse Data ===')
    for line in f:
        data = line.strip().split(',')
        print(f'Name: {data[0]}, Breed: {data[1]}, Age: {data[2]}, Height: {data[3]}m')
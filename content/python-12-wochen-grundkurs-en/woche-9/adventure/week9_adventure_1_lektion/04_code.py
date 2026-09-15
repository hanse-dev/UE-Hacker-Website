# Example 2: Line-by-line access
# Save multiple entries
hero_data = [
    'Aria,Mage,15,2500\n',
    'Thorin,Warrior,18,3200\n',
    'Luna,Rogue,12,1800\n'
]

with open('hero_list.txt', 'w') as f:
    f.writelines(hero_data)

print('✅ Hero list saved!')

# Read line by line
with open('hero_list.txt', 'r') as f:
    print('=== Hero Members ===')
    for line in f:
        data = line.strip().split(',')
        print(f'Name: {data[0]}, Class: {data[1]}, Level: {data[2]}, XP: {data[3]}')

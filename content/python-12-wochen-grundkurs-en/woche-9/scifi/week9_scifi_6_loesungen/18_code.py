# Boss Quest 1: The Mission Diary
# Note: input() replaced with fixed example values

date = '2324-03-15'
planet = 'Kepler-452b'
event = 'First soil samples collected – life signs detected'

with open('mission_diary.txt', 'w') as f:
    f.write(f'[{date}] Planet: {planet} | {event}\n')

print('Log entry saved!')

with open('mission_diary.txt', 'r') as f:
    print('\n=== Mission Diary ===')
    print(f.read())

more_entries = [
    ('2324-03-16', 'Kepler-452b', 'Contact established with alien species'),
    ('2324-03-17', 'Orbit', 'Emergency landing after meteorite impact'),
    ('2324-03-20', 'Earth', 'Return to base – mission successful'),
]

with open('mission_diary.txt', 'a') as f:
    for d, p, e in more_entries:
        f.write(f'[{d}] Planet: {p} | {e}\n')

with open('mission_diary.txt', 'r') as f:
    lines = f.readlines()

print('=== Full Mission Diary ===')
for line in lines:
    print(line.strip())

print(f'\nTotal log entries: {len(lines)}')
import json

archive = [
    {'name': 'Operation Starlight', 'planet': 'Mars', 'result': 'In Progress', 'crew': ['Shepard', 'Hicks']},
    {'name': 'Expedition Kepler', 'planet': 'Kepler-452b', 'result': 'Open', 'crew': ['Vasquez', 'Chen']},
    {'name': 'Base Alpha Setup', 'planet': 'Moon', 'result': 'Open', 'crew': ['Reyes', 'Hicks', 'Chen']},
]

with open('mission_archive.json', 'w') as f:
    json.dump(archive, f, indent=2)

print('Mission archive saved!')

with open('mission_archive.json', 'r') as f:
    loaded_archive = json.load(f)

print('\n=== Mission Archive ===')
for i, mission in enumerate(loaded_archive, 1):
    print(f'{i}. {mission["name"]}')
    print(f'   Planet: {mission["planet"]}')
    print(f'   Status: {mission["result"]}')
    print(f'   Crew: {", ".join(mission["crew"])}')

loaded_archive[0]['result'] = 'Successfully completed'

with open('mission_archive.json', 'w') as f:
    json.dump(loaded_archive, f, indent=2)

print('\n=== Final Mission Archive ===')
for mission in loaded_archive:
    status_symbol = '✅' if mission['result'] == 'Successfully completed' else '⏳'
    print(f'{status_symbol} {mission["name"]} – {mission["result"]}')

completed = [m for m in loaded_archive if m['result'] == 'Successfully completed']
with open('mission_report.txt', 'w') as f:
    f.write('=== Fleet Mission Report ===\n')
    f.write(f'Total missions: {len(loaded_archive)}\n')
    f.write(f'Completed: {len(completed)}\n')
    f.write('\nCompleted missions:\n')
    for m in completed:
        f.write(f'  - {m["name"]} (Planet: {m["planet"]})\n')

print('\nMission report saved to mission_report.txt!')
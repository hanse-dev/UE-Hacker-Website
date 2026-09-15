import json

# Step 1: Save tournament results
tournament_book = [
    {'rider': 'Lisa Müller', 'horse': 'Luna', 'placement': 1, 'discipline': 'Dressage'},
    {'rider': 'Tom Becker', 'horse': 'Spirit', 'placement': 3, 'discipline': 'Jumping'},
    {'rider': 'Sarah Klein', 'horse': 'Rocco', 'placement': 2, 'discipline': 'Dressage'},
]

with open('tournament_book.json', 'w') as f:
    json.dump(tournament_book, f, indent=2)

print('Tournament book saved!')

# Step 2: Load and display results
with open('tournament_book.json', 'r') as f:
    loaded_book = json.load(f)

print('\n=== Tournament Book ===')
for entry in loaded_book:
    medal = '🥇' if entry['placement'] == 1 else ('🥈' if entry['placement'] == 2 else '🥉')
    print(f'{medal} Place {entry["placement"]}: {entry["rider"]} with {entry["horse"]} ({entry["discipline"]})')

# Step 3: Find champions
champions = [e for e in loaded_book if e['placement'] == 1]

for champ in champions:
    champ['title'] = 'Champion'

with open('tournament_book.json', 'w') as f:
    json.dump(loaded_book, f, indent=2)

print('\n=== Final Tournament Book ===')
for entry in loaded_book:
    title = entry.get('title', '')
    print(f'  Place {entry["placement"]}: {entry["rider"]} {title}')

# Bonus: tournament report as text file
with open('tournament_report.txt', 'w') as f:
    f.write('=== Riding Ranch Tournament Report ===\n')
    f.write(f'Participants: {len(loaded_book)}\n')
    f.write('\nResults:\n')
    for entry in sorted(loaded_book, key=lambda e: e['placement']):
        f.write(f'  Place {entry["placement"]}: {entry["rider"]} with {entry["horse"]}\n')
    f.write(f'\nChampion: {champions[0]["rider"]} with {champions[0]["horse"]}!\n')

print('\nTournament report saved to tournament_report.txt!')
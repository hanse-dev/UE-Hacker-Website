import json

# Step 1: Save quests
quest_book = [
    {'name': 'The Lost Sword', 'difficulty': 'easy', 'status': 'Open'},
    {'name': 'The Ogre Threat', 'difficulty': 'medium', 'status': 'In Progress'},
    {'name': 'The Ancient Dragon Lord', 'difficulty': 'epic', 'status': 'Open'},
]

with open('quest_book.json', 'w') as f:
    json.dump(quest_book, f, indent=2)

print('Quest book saved!')

# Step 2: Load and display quests
with open('quest_book.json', 'r') as f:
    loaded_book = json.load(f)

print('\n=== Quest Book ===')
for i, quest in enumerate(loaded_book, 1):
    print(f'{i}. {quest["name"]}')
    print(f'   Difficulty: {quest["difficulty"]}')
    print(f'   Status: {quest["status"]}')

# Step 3: Complete a quest
loaded_book[1]['status'] = 'Completed'

with open('quest_book.json', 'w') as f:
    json.dump(loaded_book, f, indent=2)

print('\n=== Updated Quest Book ===')
for quest in loaded_book:
    status_symbol = '✅' if quest['status'] == 'Completed' else '⏳'
    print(f'{status_symbol} {quest["name"]} – {quest["status"]}')

# Bonus: completion report as text file
completed = [q for q in loaded_book if q['status'] == 'Completed']
with open('completion_report.txt', 'w') as f:
    f.write('=== Guild Completion Report ===\n')
    f.write(f'Completed quests: {len(completed)}\n')
    for q in completed:
        f.write(f'  - {q["name"]} (Difficulty: {q["difficulty"]})\n')

print('\nCompletion report saved to completion_report.txt!')
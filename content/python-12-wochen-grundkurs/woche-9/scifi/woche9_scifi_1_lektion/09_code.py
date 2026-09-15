# Beispiel 3: Komplexe Datenstrukturen mit JSON
raumstation = {
    'name': 'Nebula-7',
    'position': {
        'sektor': 'Alpha',
        'koordinaten': [100, 200, 300]
    },
    'crew': [
        {'name': 'Alex', 'rolle': 'Kommandant'},
        {'name': 'Zara', 'rolle': 'Wissenschaftlerin'}
    ],
    'status': 'Online'
}

# Speichern
with open('raumstation.json', 'w') as f:
    json.dump(raumstation, f, indent=2)

# Laden und analysieren
with open('raumstation.json', 'r') as f:
    station = json.load(f)

print(f'Station: {station["name"]}')
print(f'Sektor: {station["position"]["sektor"]}')
print(f'Crew-Größe: {len(station["crew"])}')
print(f'Status: {station["status"]}')
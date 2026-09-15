# Beispiel 3: Komplexe Datenstrukturen mit JSON
stall = {
    'name': 'Sonnental',
    'location': {
        'region': 'Süddeutschland',
        'koordinaten': [100, 200]
    },
    'pferde': [
        {'name': 'Thunder', 'rasse': 'Hannoveraner'},
        {'name': 'Luna', 'rasse': 'Isländer'}
    ],
    'status': 'Aktiv'
}

# Speichern
with open('stall_daten.json', 'w') as f:
    json.dump(stall, f, indent=2)

# Laden und analysieren
with open('stall_daten.json', 'r') as f:
    stall_data = json.load(f)

print(f'Stall: {stall_data['name']}')
print(f'Region: {stall_data['location']['region']}')
print(f'Pferde: {len(stall_data['pferde'])}')
print(f'Status: {stall_data['status']}')
# Beispiel 3: Komplexe Datenstrukturen mit JSON
gilde = {
    'name': 'Helden von Pyralia',
    'location': {
        'region': 'Zentralpyralia',
        'koordinaten': [100, 200]
    },
    'mitglieder': [
        {'name': 'Aria', 'rolle': 'Magierin'},
        {'name': 'Thorin', 'rolle': 'Krieger'}
    ],
    'status': 'Aktiv'
}

# Speichern
with open('gilde_daten.json', 'w') as f:
    json.dump(gilde, f, indent=2)

# Laden und analysieren
with open('gilde_daten.json', 'r') as f:
    gilde_data = json.load(f)

print(f'Gilde: {gilde_data['name']}')
print(f'Region: {gilde_data['location']['region']}')
print(f'Mitglieder: {len(gilde_data['mitglieder'])}')
print(f'Status: {gilde_data['status']}')
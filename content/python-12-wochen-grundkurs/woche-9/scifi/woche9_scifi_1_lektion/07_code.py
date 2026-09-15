# 🔍 Übungen mit JSON
import json

# Beispiel 1: Dictionary zu JSON
schiff = {
    'name': 'Nebula-Explorer',
    'typ': 'Forschung',
    'crew': 150,
    'systeme': ['Antrieb', 'Leben', 'Kommunikation']
}

# Zu JSON-String konvertieren
json_string = json.dumps(schiff, indent=2)
print('=== JSON-String ===')
print(json_string)

# Zurück zu Dictionary
zurueck = json.loads(json_string)
print(f'\nName: {zurueck["name"]}')
# 🔍 Übungen mit JSON
import json

# Beispiel 1: Dictionary zu JSON
pferd = {
    'name': 'Thunder',
    'rasse': 'Hannoveraner',
    'alter': 8,
    'groesse': 1.72,
    'faehigkeiten': ['Dressur', 'Springen', 'Western']
}

# Zu JSON-String konvertieren
json_string = json.dumps(pferd, indent=2)
print('=== JSON-String ===')
print(json_string)

# Zurück zu Dictionary
zurueck = json.loads(json_string)
print(f'\nName: {zurueck['name']}')
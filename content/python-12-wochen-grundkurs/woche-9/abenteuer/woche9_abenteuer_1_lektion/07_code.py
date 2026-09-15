# 🔍 Übungen mit JSON
import json

# Beispiel 1: Dictionary zu JSON
held = {
    'name': 'Aria',
    'klasse': 'Magierin',
    'level': 15,
    'faehigkeiten': ['Feuerball', 'Heilung', 'Schild']
}

# Zu JSON-String konvertieren
json_string = json.dumps(held, indent=2)
print('=== JSON-String ===')
print(json_string)

# Zurück zu Dictionary
zurueck = json.loads(json_string)
print(f'\nName: {zurueck['name']}')
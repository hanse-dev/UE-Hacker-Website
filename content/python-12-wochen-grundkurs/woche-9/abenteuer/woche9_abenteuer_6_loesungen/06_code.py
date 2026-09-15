# Problem: load() erwartet Schriftrolle, nicht String
import json
daten = {'name': 'Test'}
json_string = json.dumps(daten)
ergebnis = json.loads(json_string)  # loads() für String
print(f'Ergebnis: {ergebnis}')
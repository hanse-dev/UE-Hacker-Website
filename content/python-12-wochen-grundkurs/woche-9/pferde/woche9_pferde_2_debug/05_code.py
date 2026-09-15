import json
daten = {'name': 'Test'}
json_string = json.dumps(daten)
ergebnis = json.load(json_string)
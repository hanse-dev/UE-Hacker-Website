# Beispiel 2: JSON-Dateien schreiben und lesen
# In Datei speichern
with open('schiff_daten.json', 'w') as f:
    json.dump(schiff, f, indent=2)

print('✅ Schiff-Daten gespeichert!')

# Aus Datei laden
with open('schiff_daten.json', 'r') as f:
    geladen = json.load(f)

print('=== Geladene Daten ===')
print(f'Schiff: {geladen["name"]}')
print(f'Systeme: {", ".join(geladen["systeme"])}')
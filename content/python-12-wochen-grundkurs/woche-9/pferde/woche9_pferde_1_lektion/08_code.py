# Beispiel 2: JSON-Dateien schreiben und lesen
# In Datei speichern
with open('pferd_daten.json', 'w') as f:
    json.dump(pferd, f, indent=2)

print('✅ Pferd-Daten gespeichert!')

# Aus Datei laden
with open('pferd_daten.json', 'r') as f:
    geladen = json.load(f)

print('=== Geladene Daten ===')
print(f'Pferd: {geladen['name']}')
print(f'Fähigkeiten: {', '.join(geladen['faehigkeiten'])}')
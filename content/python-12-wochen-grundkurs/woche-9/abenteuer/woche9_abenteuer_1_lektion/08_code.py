# Beispiel 2: JSON-Schriftrollen schreiben und lesen
# In Schriftrolle speichern
with open('held_daten.json', 'w') as f:
    json.dump(held, f, indent=2)

print('✅ Held-Daten gespeichert!')

# Aus Schriftrolle laden
with open('held_daten.json', 'r') as f:
    geladen = json.load(f)

print('=== Geladene Daten ===')
print(f'Held: {geladen['name']}')
print(f'Fähigkeiten: {', '.join(geladen['faehigkeiten'])}')
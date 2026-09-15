# Beispiel 3: Artefakt unpacking und Methoden
held_daten = ("Aria", "Magierin", 15, 120)

# Artefakt unpacking
name, klasse, level, lebenspunkte = held_daten
print("=== Artefakt Unpacking ===")
print(f"Name: {name}")
print(f"Klasse: {klasse}")
print(f"Level: {level}")
print(f"Lebenspunkte: {lebenspunkte}")

# Artefakt-Methoden
print(f"\nAnzahl Elemente: {len(held_daten)}")
print(f"Index von 'Magierin': {held_daten.index('Magierin')}")
print(f"Anzahl 'Magierin': {held_daten.count('Magierin')}")
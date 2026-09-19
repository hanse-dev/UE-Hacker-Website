# Beispiel 1: Schleife oder List Comprehension – gleiches Ergebnis
schaden = [3, 7, 12, 5]

# Mit Schleife und append (Woche 4 + 6):
verdoppelt_schleife = []
for wert in schaden:
    verdoppelt_schleife.append(wert * 2)

# Mit List Comprehension – nur eine Zeile:
verdoppelt = [wert * 2 for wert in schaden]
print(f"Schleife: {verdoppelt_schleife}")
print(f"Comprehension: {verdoppelt}")

# Beispiel 2: Jedes Element umwandeln
inventar = ["Trank", "Schwert", "Schlüssel", "Schatz", "Karte"]
grossbuchstaben = [w.upper() for w in inventar]
print(f"\nLaut gerufen: {grossbuchstaben}")

# Beispiel 3: Filtern mit if
lange_namen = [w for w in inventar if len(w) > 5]
print(f"Lange Namen: {lange_namen}")

# Beispiel 4: Umwandeln UND filtern
grosse_werte = [wert * 2 for wert in schaden if wert > 4]
print(f"Verdoppelte Werte über 4: {grosse_werte}")

# Die Original-Liste bleibt unverändert
print(f"\nOriginal (Schaden): {schaden}")
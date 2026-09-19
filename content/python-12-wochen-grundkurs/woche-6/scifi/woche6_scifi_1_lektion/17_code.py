# Beispiel 1: Schleife oder List Comprehension – gleiches Ergebnis
energie = [40, 75, 20, 90]

# Mit Schleife und append (Woche 4 + 6):
verdoppelt_schleife = []
for wert in energie:
    verdoppelt_schleife.append(wert * 2)

# Mit List Comprehension – nur eine Zeile:
verdoppelt = [wert * 2 for wert in energie]
print(f"Schleife: {verdoppelt_schleife}")
print(f"Comprehension: {verdoppelt}")

# Beispiel 2: Jedes Element umwandeln
systeme = ["Waffensystem", "Schild", "Antrieb", "Sensor"]
grossbuchstaben = [w.upper() for w in systeme]
print(f"\nGroß geschrieben: {grossbuchstaben}")

# Beispiel 3: Filtern mit if
lange_namen = [w for w in systeme if len(w) > 6]
print(f"Lange Namen: {lange_namen}")

# Beispiel 4: Umwandeln UND filtern
grosse_werte = [wert * 2 for wert in energie if wert > 50]
print(f"Verdoppelte Werte über 50: {grosse_werte}")

# Die Original-Liste bleibt unverändert
print(f"\nOriginal (Energie): {energie}")
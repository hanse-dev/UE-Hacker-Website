# Beispiel 1: Schleife oder List Comprehension – gleiches Ergebnis
punkte = [6, 9, 7, 10]

# Mit Schleife und append (Woche 4 + 6):
verdoppelt_schleife = []
for wert in punkte:
    verdoppelt_schleife.append(wert * 2)

# Mit List Comprehension – nur eine Zeile:
verdoppelt = [wert * 2 for wert in punkte]
print(f"Schleife: {verdoppelt_schleife}")
print(f"Comprehension: {verdoppelt}")

# Beispiel 2: Jedes Element umwandeln
disziplinen = ["Dressur", "Springen", "Vielseitigkeit", "Voltigieren"]
grossbuchstaben = [w.upper() for w in disziplinen]
print(f"\nGroß geschrieben: {grossbuchstaben}")

# Beispiel 3: Filtern mit if
lange_namen = [w for w in disziplinen if len(w) > 7]
print(f"Lange Namen: {lange_namen}")

# Beispiel 4: Umwandeln UND filtern
grosse_werte = [wert * 2 for wert in punkte if wert > 7]
print(f"Verdoppelte Werte über 7: {grosse_werte}")

# Die Original-Liste bleibt unverändert
print(f"\nOriginal (Punkte): {punkte}")
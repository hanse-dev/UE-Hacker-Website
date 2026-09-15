# Schritt 1 – Flugdaten sammeln
shuttle_nummer = "SH-09"
ziel = "Raumstation Delta"
pilot = "Chen"
fracht = "Medizinische Vorräte"

# Schritt 2 – Protokoll-Kopf
print("=== FLUGPROTOKOLL ===")
print()

# Schritt 3 – Missionsbeschreibung
print("Shuttle " + shuttle_nummer + " startet in Kürze.")
print("Pilot " + pilot + " fliegt Richtung " + ziel + ".")
print("An Bord befindet sich: " + fracht + ".")

# Schritt 4 – Countdown
print()
print("Start in:")
print("3... 2... 1... Start!")

# Bonus – Koordinaten
x = 347
y = 892
z = 15
print()
print("Zielkoordinaten – X: " + str(x) + " Y: " + str(y) + " Z: " + str(z))
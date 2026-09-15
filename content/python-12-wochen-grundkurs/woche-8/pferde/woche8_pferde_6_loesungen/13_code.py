import math

# Schritt 1: Koordinaten als Tupel
pos1 = (0, 0)      # Stall
pos2 = (50, 30)    # Reitplatz
print(f"Startpunkt (Stall):    {pos1} | Länge: {len(pos1)}")
print(f"Endpunkt (Reitplatz):  {pos2} | Länge: {len(pos2)}")

# Schritt 2: Tupel-Unpacking
x1, y1 = pos1
print(f"\nStall: x={x1}, y={y1}")
x2, y2 = pos2
print(f"Reitplatz: x={x2}, y={y2}")

# Schritt 3: Positions-Dictionary
positionen = {
    "Stall": (0, 0),
    "Reitplatz": (50, 30),
    "Weide": (100, 80),
    "Turnierbahn": (200, 150)
}
print(f"\nPositions-Dictionary: {positionen}")
print(f"Reitplatz-Position: {positionen['Reitplatz']}")

# Schritt 4: Abstandsberechnung
def abstand(koord1, koord2):
    x1, y1 = koord1
    x2, y2 = koord2
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

a = abstand(positionen["Stall"], positionen["Reitplatz"])
print(f"\nAbstand Stall → Reitplatz: {a} m")
b = abstand(positionen["Reitplatz"], positionen["Weide"])
print(f"Abstand Reitplatz → Weide: {b} m")

# Bonus: 3D-Koordinaten
pos_3d_1 = (0, 0, 0)
pos_3d_2 = (50, 30, 10)
x1, y1, z1 = pos_3d_1
x2, y2, z2 = pos_3d_2
abstand_3d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 2)
print(f"\nBonus 3D-Abstand: {abstand_3d} m")
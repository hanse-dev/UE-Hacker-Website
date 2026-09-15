# Schritt 1: 3D-Koordinaten als Tupel
pos1 = (100, 200, 50)
pos2 = (300, -150, 80)
print(f"Position 1: {pos1}, Länge: {len(pos1)}")
print(f"Position 2: {pos2}, Länge: {len(pos2)}")

# Schritt 2: Tupel-Unpacking
x1, y1, z1 = pos1
print(f"X={x1}, Y={y1}, Z={z1}")

# Schritt 3: Kombination mit Dictionary
koordinaten = {
    "start": pos1,
    "ziel": pos2,
    "entfernung": ((x1 - pos2[0])**2 + (y1 - pos2[1])**2 + (z1 - pos2[2])**2) ** 0.5
}
print(f"\nRoute: {koordinaten['start']} → {koordinaten['ziel']}")
print(f"Entfernung: {koordinaten['entfernung']:.1f} Lichtjahre")
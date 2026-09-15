# Beispiel 2: Auf Listenelemente zugreifen
ausruestung = ["Phaser", "Tricorder", "Kommunikator", "Medi-Kit", "Werkzeug"]

print("=== Ausrüstungs-Zugriff ===")
print(f"Gesamte Ausrüstung: {ausruestung}")
print(f"Erstes Item: {ausruestung[0]}")
print(f"Zweites Item: {ausruestung[1]}")
print(f"Letztes Item: {ausruestung[-1]}")

# Länge der Liste
print(f"Anzahl Items: {len(ausruestung)}")

# Slicing (Ausschnitte)
print(f"Erste 3 Items: {ausruestung[0:3]}")
print(f"Letzte 2 Items: {ausruestung[-2:]}")
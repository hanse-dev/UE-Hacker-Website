# Beispiel 3: Listen kombinieren
schaetze = ["Gold", "Silber", "Edelsteine"]
waffen = ["Schwert", "Bogen", "Axt"]
tränke = ["Heilung", "Mana", "Stärke"]

print("=== Listen kombinieren ===")
print(f"Schätze: {schaetze}")
print(f"Waffen: {waffen}")
print(f"Tränke: {tränke}")

# Mit + Operator kombinieren
alles = schaetze + waffen + tränke
print(f"Alles kombiniert: {alles}")

# Mit extend() eine Liste zur anderen hinzufügen
schaetze.extend(waffen)
print(f"Schätze erweitert: {schaetze}")
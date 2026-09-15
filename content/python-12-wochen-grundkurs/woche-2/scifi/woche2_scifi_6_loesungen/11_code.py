# Schritt 1 – Techniker identifizieren
techniker = "Chief Engineer Ryo"
techniker_id = 5503

# Schritt 2 – Energieblöcke erfassen
anzahl_bloecke = 6
energie_pro_block = 45.5

# Schritt 3 – Gesamtenergie berechnen
gesamtenergie = anzahl_bloecke * energie_pro_block

print(f"Techniker: {techniker} (ID: {techniker_id})")
print(f"Energieblöcke: {anzahl_bloecke}")
print(f"Energie pro Block: {energie_pro_block} TW")
print(f"Gesamtenergie: {gesamtenergie} TW")

# Bonus
kuehl_pro_block = 12.0
gesamt_kuehlung = anzahl_bloecke * kuehl_pro_block
print(f"Gesamtkühlleistung: {gesamt_kuehlung} MW")
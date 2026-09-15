# Beispiel 1: In Listen suchen
inventar = ["Schwert", "Schild", "Trank", "Bogen", "Schwert", "Pfeile"]

print("=== In Listen suchen ===")
print(f"Inventar: {inventar}")

# Mit index() Position finden
position_schild = inventar.index("Schild")
print(f"Schild an Position: {position_schild}")

# Mit in() prüfen ob vorhanden
hat_bogen = "Bogen" in inventar
hat_zauberstab = "Zauberstab" in inventar
print(f"Bogen vorhanden: {hat_bogen}")
print(f"Zauberstab vorhanden: {hat_zauberstab}")

# Mit count() zählen
anzahl_schwerter = inventar.count("Schwert")
print(f"Anzahl Schwerter: {anzahl_schwerter}")
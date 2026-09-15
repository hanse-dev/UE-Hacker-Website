# Beispiel 1: In Listen suchen
pferde = ["Thunder", "Luna", "Storm", "Shadow", "Thunder", "Luna"]

print("=== In Listen suchen ===")
print(f"Pferde-Liste: {pferde}")

# Mit index() Position finden
position_luna = pferde.index("Luna")
print(f"Luna an Position: {position_luna}")

# Mit in() prüfen ob vorhanden
hat_storm = "Storm" in pferde
hat_bobby = "Bobby" in pferde
print(f"Storm vorhanden: {hat_storm}")
print(f"Bobby vorhanden: {hat_bobby}")

# Mit count() zählen
anzahl_thunder = pferde.count("Thunder")
print(f"Anzahl Thunder: {anzahl_thunder}")
# Beispiel 1: In Listen suchen
systeme = ["Waffensystem", "Schildsystem", "Antriebssystem", "Lebenserhaltung", "Waffensystem", "Antriebssystem"]

print("=== In Listen suchen ===")
print(f"System-Liste: {systeme}")

# Mit index() Position finden
position_schild = systeme.index("Schildsystem")
print(f"Schildsystem an Position: {position_schild}")

# Mit in() prüfen ob vorhanden
hat_antrieb = "Antriebssystem" in systeme
hat_teleporter = "Teleporter" in systeme
print(f"Antriebssystem vorhanden: {hat_antrieb}")
print(f"Teleporter vorhanden: {hat_teleporter}")

# Mit count() zählen
anzahl_waffen = systeme.count("Waffensystem")
print(f"Anzahl Waffensysteme: {anzahl_waffen}")
# 🔍 Übungen mit append() und insert()

# Beispiel 1: Elemente hinzufügen
missions_log = []
print(f"Leeres Missions-Log: {missions_log}")

# Mit append() am Ende hinzufügen
missions_log.append("Planetenerkundung")
print(f"Nach append: {missions_log}")

missions_log.append("Asteroidenabbau")
missions_log.append("Erste-Kontakt-Mission")
print(f"Voll gefüllt: {missions_log}")

# Mit insert() an bestimmter Position einfügen
missions_log.insert(0, "System-Check")  # Am Anfang
print(f"Nach insert(0): {missions_log}")

missions_log.insert(2, "Wartung")  # An Position 2
print(f"Nach insert(2): {missions_log}")
def erstelle_mission(name, ziel, prioritaet):
    return {"name": name, "ziel": ziel, "prioritaet": prioritaet, "status": "aktiv"}

missionen = [
    erstelle_mission("Operation Nova", "Andromeda-Cluster", 5),
    erstelle_mission("Aufklärung X", "Oort-Gürtel", 2),
    erstelle_mission("Rettung Alpha", "Titan-Station", 4),
]

print("=== Missions-Datenbank ===")
for m in missionen:
    print(f"  {m['name']} | Ziel: {m['ziel']} | Prio: {m['prioritaet']}")

hoch_prio = [m for m in missionen if m["prioritaet"] >= 4]
print(f"\nHoch-Priorität: {[m['name'] for m in hoch_prio]}")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Daten-Archivar der unendlichen Arrays besiegt!")
print("⭐ Titel erhalten: Meister der Daten-Sammlungen")
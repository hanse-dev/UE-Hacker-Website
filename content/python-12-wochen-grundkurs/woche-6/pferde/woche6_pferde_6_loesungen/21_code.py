def erstelle_turnier(name, disziplin, schwierigkeit):
    return {"name": name, "disziplin": disziplin, "schwierigkeit": schwierigkeit, "status": "offen"}

turniere = [
    erstelle_turnier("Frühlingspokal", "Dressur", 3),
    erstelle_turnier("Sommerturnier", "Springen", 4),
    erstelle_turnier("Herbstcup", "Vielseitigkeit", 5),
]

print("=== Turnier-Datenbank ===")
for t in turniere:
    print(f"  {t['name']} | {t['disziplin']} | Schwierigkeit: {t['schwierigkeit']}")

# Suchen
schwer = [t for t in turniere if t["schwierigkeit"] >= 4]
print(f"\nSchwere Turniere: {[t['name'] for t in schwer]}")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Stallmeister der unendlichen Listen besiegt!")
print("⭐ Titel erhalten: Meister der Trainings-Sammlungen")
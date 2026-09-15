import random
import math

hindernistypen = ["Stange", "Wassergraben", "Kurve", "Doppelstange", "Mauer"]
schwierigkeiten = [1, 2, 3, 4, 5]

# Schritt 1 & 2: Parcours erstellen und ausgeben
print("=== ZUFALLS-PARCOURS ===")
gesamt_schwierigkeit = 0
for i in range(1, 7):
    typ = random.choice(hindernistypen)
    schwierigkeit = random.choice(schwierigkeiten)
    gesamt_schwierigkeit += schwierigkeit
    print(f"Hindernis {i}: {typ} | Schwierigkeit: {schwierigkeit}/5")

# Schritt 3: Gesamtschwierigkeit und Technikfaktor
technikfaktor = round(math.sqrt(gesamt_schwierigkeit), 2)
print(f"\nGesamtschwierigkeit: {gesamt_schwierigkeit}")
print(f"Technikfaktor:       {technikfaktor}")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Schmied der unendlichen Werkzeuge besiegt!")
print("⭐ Titel erhalten: Meister der Werkzeugkisten")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 7 gemeistert!")
print("📚 Nächste Woche: Dictionaries und Tupel!")
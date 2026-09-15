import random
import math

sektor_typen = ["Asteroidenfeld", "Nebel", "Freier Raum", "Ionensturm", "Ruhezone"]
ereignisse = ["Feindkontakt", "Ressourcenfund", "Leerer Sektor", "Notsignal", "Ruhig"]
gefaehrliche_sektoren = ["Asteroidenfeld", "Ionensturm", "Feindkontakt"]

print("=== ERKUNDUNGSBERICHT ===")
treibstoff = 0
for i in range(1, 6):
    typ = random.choice(sektor_typen)
    ereignis = random.choice(ereignisse)
    ist_gefaehrlich = typ in gefaehrliche_sektoren or ereignis in gefaehrliche_sektoren
    kosten = 2 if ist_gefaehrlich else 1
    treibstoff += kosten
    status = "⚠️ GEFÄHRLICH" if ist_gefaehrlich else "✓ Sicher"
    print(f"Sektor {i}: {typ} | {ereignis} | {status} | Kosten: {kosten}")

print(f"\nGesamter Treibstoffverbrauch: {math.ceil(treibstoff)} Einheiten")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Code-Archivar der unendlichen Funktionen besiegt!")
print("⭐ Titel erhalten: Meister der Module")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 7 gemeistert!")
print("📚 Nächste Woche: Dictionaries und Tupel!")
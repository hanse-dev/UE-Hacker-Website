import random

# Schritt 1 – Begrüßungsfunktion
def begruesse_besatzung():
    print("Willkommen an Bord der Nebula-7!")
    print("Alle Systeme bereit – Einsatz kann beginnen.")

begruesse_besatzung()
begruesse_besatzung()

# Schritt 2 – Energie-Berechnung
def berechne_energie(level, dauer):
    return level * dauer * 10

# Schritt 3 – System-Status prüfen
def ist_system_bereit(energie):
    return energie >= 100

# Schritt 4 – Hauptprogramm
energie = berechne_energie(4, 5)
print(f"Berechnete Energie: {energie} Einheiten")

if ist_system_bereit(energie):
    print("System-Status: BEREIT")
else:
    print("System-Status: NICHT BEREIT – zu wenig Energie")

# Bonus – zufälliges Systemereignis
def generiere_systemereignis():
    ereignisse = ["Sonnensturm", "Sensorfehler", "Alles stabil", "Mikrometeor-Alarm", "Kühlsystem-Warnung"]
    return random.choice(ereignisse)

print(f"Aktuelles Ereignis: {generiere_systemereignis()}")
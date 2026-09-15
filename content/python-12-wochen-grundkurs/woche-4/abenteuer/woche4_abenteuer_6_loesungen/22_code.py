import random

# Schritt 1 – Startbedingungen
leben = 100
mana = 80
tiefe = 0
gesamtschatz = 0
besondere_ereignisse = []

print("=== DER UNENDLICHE DUNGEON ===")
print(f"Start: Leben={leben}, Mana={mana}")
print()

# Schritt 1 – Endlosschleife
while True:
    tiefe += 1

    # Schritt 2 – Zufälliger Schatzwert
    schatz = random.randint(5, 50)
    gesamtschatz += schatz

    # Schritt 2 – Leben und Mana verbrauchen
    schaden = random.randint(5, 20)
    mana_verlust = random.randint(3, 10)
    leben -= schaden
    mana -= mana_verlust

    # Schritt 4 – Heilungsquellen alle 5 Räume
    if tiefe % 5 == 0:
        heilung = random.randint(15, 30)
        leben += heilung
        if leben > 100:
            leben = 100
        ereignis = f"Raum {tiefe}: Heilquelle! +{heilung} Leben"
        besondere_ereignisse.append(ereignis)
        print(ereignis)

    # Schritt 3 – Tod prüfen
    if leben <= 0:
        print(f"💀 Held stirbt in Raum {tiefe}! Schatz: {gesamtschatz} Gold")
        break

    if mana <= 0:
        print(f"🔮 Mana erschöpft in Raum {tiefe}! Schatz: {gesamtschatz} Gold")
        break

    # Statusanzeige alle 10 Räume
    if tiefe % 10 == 0:
        print(f"Tiefe {tiefe}: Leben={leben}, Mana={mana}, Schatz={gesamtschatz}")

    if tiefe >= 100:
        print(f"🏆 Dungeon-Legende! {tiefe} Räume überlebt!")
        break

print()
print("=== DUNGEON-AUSWERTUNG ===")
print(f"Erreichte Tiefe: {tiefe} Räume")
print(f"Gesamtschatz: {gesamtschatz} Gold")
print(f"Besondere Ereignisse: {len(besondere_ereignisse)}")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den unendlichen Zyklop besiegt!")
print("⭐ Titel erhalten: Meister der Kreisläufe")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 4 gemeistert!")
print("📚 Nächste Woche: Funktionen (def, return)!")
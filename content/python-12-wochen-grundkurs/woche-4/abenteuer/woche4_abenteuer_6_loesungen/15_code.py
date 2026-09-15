import random

# Schritt 1 – Variablen
schritte = 0
position = [0, 0]  # [x, y]
ausgangs_position = [0, 0]
richtungen = ["Norden", "Süden", "Osten", "Westen"]
besuchte_positionen = []

# Starte etwas weg vom Ausgang
position = [3, 2]

# Schritt 1 – Haupt-Loop
while True:
    schritte += 1

    # Schritt 2 – Zufällige Richtung
    richtung = random.choice(richtungen)
    if richtung == "Norden":
        position[1] += 1
    elif richtung == "Süden":
        position[1] -= 1
    elif richtung == "Osten":
        position[0] += 1
    else:  # Westen
        position[0] -= 1

    besuchte_positionen.append([position[0], position[1]])

    # Schritt 4 – Statusmeldung alle 10 Schritte
    if schritte % 10 == 0:
        print(f"Schritt {schritte}: Position ({position[0]}, {position[1]})")

    # Schritt 3 – Ausgang gefunden?
    if position == ausgangs_position:
        print(f"🎉 Ausgang gefunden nach {schritte} Schritten!")
        break

    # Schritt 3 – Nach 100 Schritten aufgeben
    if schritte >= 100:
        print(f"😵 Verloren im Labyrinth nach {schritte} Schritten!")
        break

print(f"Insgesamt {len(besuchte_positionen)} verschiedene Felder besucht.")
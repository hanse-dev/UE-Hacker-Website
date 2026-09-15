# Schritt 1 – Turnierdaten
punkte = 90
fehler = 0
zeit = 55  # Sekunden

# Schritt 2 – Gesamtnote
note = punkte - (fehler * 5) - (zeit / 10)
print(f"Punkte: {punkte}, Fehler: {fehler}, Zeit: {zeit}s")
print(f"Gesamtnote: {note:.1f}")

# Schritt 3 – Gold-Medaille
if note >= 85 and fehler == 0:
    print("🥇 GOLD! Traumhafter Ritt!")
elif note >= 70 and fehler <= 2:
    print("🥈 SILBER! Sehr guter Ritt!")
elif note >= 50:
    print("🥉 BRONZE! Solider Ritt.")
else:
    print("Leider keine Medaille diesmal.")

# Schritt 5 – Perfekte-Zeit-Bonus
if zeit < 60:
    print("+10 Bonus für perfekte Zeit!")
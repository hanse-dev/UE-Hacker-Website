# Schritt 1–4 – Rundgang durch alle Boxen
for box in range(1, 11):
    # Schritt 3 – Box 7 überspringen (Renovierung)
    if box == 7:
        print("Box 7: 🔧 In Renovierung – wird übersprungen!")
        continue

    # Schritt 1 – Standardmeldung
    print(f"Box {box}: Kontrolle läuft...")

    # Schritt 2 – Extra-Kontrolle bei 3, 6, 9
    if box in [3, 6, 9]:
        print(f"  ⚠️ Box {box}: Extra-Kontrolle nötig!")

    # Schritt 2 – Bonus bei Box 5 und 10
    if box in [5, 10]:
        print(f"  🎁 Bonus für besonders saubere Box {box}!")

    # Schritt 4 – Bei Box 10 beenden
    if box == 10:
        break

print()
print("✅ Alle wichtigen Boxen überprüft!")
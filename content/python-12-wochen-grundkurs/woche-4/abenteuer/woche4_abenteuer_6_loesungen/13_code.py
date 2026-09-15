# Schritt 1–4 – Turmaufstieg durch alle Stockwerke
for stockwerk in range(1, 11):
    # Schritt 3 – Stockwerk 7 überspringen
    if stockwerk == 7:
        print("Stockwerk 7: 🔧 Wegen magischer Reparatur gesperrt – übersprungen!")
        continue

    # Schritt 2 – Standardmeldung
    print(f"Stockwerk {stockwerk}: Alles ruhig...")

    # Schritt 2 – Warnungen bei 3, 6, 9
    if stockwerk in [3, 6, 9]:
        print(f"  ⚠️ Magische Störung auf Stockwerk {stockwerk}!")

    # Schritt 2 – Bonus bei 5 und 10
    if stockwerk in [5, 10]:
        print(f"  🎁 Verborgener Schatz auf Stockwerk {stockwerk} entdeckt!")

    # Schritt 4 – Bei Stockwerk 10 beenden
    if stockwerk == 10:
        break

print()
print("✅ Du hast den Turm bezwungen!")
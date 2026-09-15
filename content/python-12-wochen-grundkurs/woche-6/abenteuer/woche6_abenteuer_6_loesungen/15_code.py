# Schritt 1 – Gilden-Liste anlegen
gilde = [
    ["Aldric", "Krieger", 8],
    ["Lyra", "Magierin", 6],
    ["Toryn", "Schurke", 10],
]
print("Gildenmitglieder:")
for held in gilde:
    print(f"  {held[0]} ({held[1]}) – Level {held[2]}")

# Schritt 2 – Helden erweitern
gilde.append(["Sera", "Heilerin", 5])
print(f"\nNach Beitritt: {len(gilde)} Mitglieder")

# Schritt 3 – Helden durchsuchen und sortieren
such_name = "Lyra"
position = next((i for i, h in enumerate(gilde) if h[0] == such_name), -1)
print(f"Position von {such_name}: {position}")

sortiert = sorted(gilde, key=lambda h: h[2], reverse=True)
print("Sortiert nach Level (absteigend):")
for h in sortiert:
    print(f"  {h[0]} – Level {h[2]}")

# Schritt 4 – Statistik
print(f"\nGesamtmitglieder: {len(gilde)}")
klassen = [h[1] for h in gilde]
print(f"Klassen: {', '.join(klassen)}")
durchschnitt_level = sum(h[2] for h in gilde) / len(gilde)
print(f"Durchschnittslevel: {durchschnitt_level:.1f}")

# Bonus – Missionen-Spalte und Sortierung
for held in gilde:
    held.append(held[2] * 3)  # Missionen = Level * 3 als Beispiel
print("\nNach Missionen sortiert:")
for h in sorted(gilde, key=lambda x: x[3], reverse=True):
    print(f"  {h[0]}: {h[3]} Missionen")
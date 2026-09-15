# Schritt 1: Helden-Liste anlegen
helden = [
    {"name": "Thorin", "klasse": "Krieger", "level": 8, "erfahrung": 2400},
    {"name": "Aria", "klasse": "Magierin", "level": 6, "erfahrung": 1800},
    {"name": "Lyra", "klasse": "Bogenschützin", "level": 7, "erfahrung": 2100},
]
print("=== HELDEN-GILDE ===")
for h in helden:
    print(f"  {h['name']} | {h['klasse']} | Level {h['level']}")

# Schritt 2: Mitglied hinzufügen
helden.append({"name": "Drake", "klasse": "Krieger", "level": 4, "erfahrung": 900})
print(f"\nMitglieder nach Beitritt: {len(helden)}")

# Schritt 3: Suchfunktion nach Klasse
def suche_nach_klasse(helden_liste, klasse):
    return [h for h in helden_liste if h["klasse"] == klasse]

krieger = suche_nach_klasse(helden, "Krieger")
print("\nAlle Krieger:")
for k in krieger:
    print(f"  {k['name']} (Level {k['level']})")

magier = suche_nach_klasse(helden, "Magierin")
print("\nAlle Magierinnen:")
for m in magier:
    print(f"  {m['name']} (Level {m['level']})")

# Schritt 4: Durchschnittslevel
durchschnitt_level = sum(h["level"] for h in helden) / len(helden)
print(f"\nDurchschnittslevel der Gilde: {durchschnitt_level:.1f}")

# Quest zuweisen
for h in helden:
    if h["level"] >= 7:
        h["quest"] = "Drache besiegen"
    else:
        h["quest"] = "Banditencamp säubern"

print("\nQuest-Zuweisung:")
for h in helden:
    print(f"  {h['name']}: {h['quest']}")

# Bonus: Fähigkeiten
helden[0]["faehigkeiten"] = ["Schildwall", "Berserker", "Eiserner Wille"]
print(f"\nBonus – Fähigkeiten von {helden[0]['name']}: {helden[0]['faehigkeiten']}")
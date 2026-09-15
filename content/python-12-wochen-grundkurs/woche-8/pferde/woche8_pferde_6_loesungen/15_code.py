# Schritt 1: Reiter-Liste anlegen
reiter = [
    {"name": "Lena", "level": 3, "alter": 16, "erfahrung": 4},
    {"name": "Tom", "level": 2, "alter": 14, "erfahrung": 2},
    {"name": "Sophie", "level": 3, "alter": 18, "erfahrung": 5}
]
print("=== REITER-GILDE ===")
for r in reiter:
    print(f"  {r['name']} | Level {r['level']} | {r['erfahrung']} Jahre Erfahrung")

# Schritt 2: Mitglied hinzufügen
reiter.append({"name": "Max", "level": 1, "alter": 12, "erfahrung": 1})
print(f"\nMitglieder nach Beitritt: {len(reiter)}")

# Schritt 3: Suchfunktion nach Level
def suche_nach_level(reiter_liste, level):
    return [r for r in reiter_liste if r["level"] == level]

level3_reiter = suche_nach_level(reiter, 3)
print("\nAlle Reiter auf Level 3:")
for r in level3_reiter:
    print(f"  {r['name']} (Alter {r['alter']})")

level2_reiter = suche_nach_level(reiter, 2)
print("\nAlle Reiter auf Level 2:")
for r in level2_reiter:
    print(f"  {r['name']} (Alter {r['alter']})")

# Schritt 4: Durchschnittsalter
durchschnitt_alter = sum(r["alter"] for r in reiter) / len(reiter)
print(f"\nDurchschnittsalter: {durchschnitt_alter:.1f} Jahre")

# Pferd zuweisen
pferde_namen = ["Thunder", "Luna", "Blitz", "Silber"]
for i, r in enumerate(reiter):
    r["pferd"] = pferde_namen[i]

print("\nPferd-Zuweisung:")
for r in reiter:
    print(f"  {r['name']} reitet {r['pferd']}")

# Bonus: Turniere
reiter[0]["turniere"] = ["Frühjahrsturnier 2024", "Herbst-Cup", "Kreismeisterschaft"]
print(f"\nBonus – Turniere von {reiter[0]['name']}: {reiter[0]['turniere']}")
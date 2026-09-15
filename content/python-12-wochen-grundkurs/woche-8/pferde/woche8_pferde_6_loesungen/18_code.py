# Schritt 1: Steckbrief anlegen
thunder = {"name": "Thunder", "rasse": "Hannoveraner", "alter": 8, "disziplin": "Dressur"}
print("=== STALLARCHIV ===")
for key, val in thunder.items():
    print(f"  {key}: {val}")

# Schritt 2: Stall befüllen
stall = [
    {"name": "Thunder", "rasse": "Hannoveraner", "alter": 8, "disziplin": "Dressur"},
    {"name": "Luna", "rasse": "Isländer", "alter": 4, "disziplin": "Geländeritt"},
    {"name": "Blitz", "rasse": "Araber", "alter": 6, "disziplin": "Springen"}
]

# Schritt 3: Pferde älter als 5 Jahre
print("\nPferde älter als 5 Jahre:")
gesamtalter = 0
for p in stall:
    gesamtalter += p["alter"]
    if p["alter"] > 5:
        print(f"  {p['name']}: {p['alter']} Jahre ({p['rasse']})")
durchschnitt = gesamtalter / len(stall)
print(f"Durchschnittsalter: {durchschnitt:.1f} Jahre")

# Bonus: Sortierung nach Alter (jüngstes zuerst)
sortiert = sorted(stall, key=lambda p: p["alter"])
print("\nSortiert nach Alter (jüngstes zuerst):")
for p in sortiert:
    print(f"  {p['name']}: {p['alter']} Jahre")
# Schritt 1: Crew-Liste (verschachtelt: [Name, Rang, Position])
crew = [
    ["Captain Alex", "Kommandant", "Alpha"],
    ["Dr. Vega", "Medizinerin", "Beta"],
    ["Tech Orion", "Ingenieur", "Gamma"],
]
print("=== Crew-Datenbank ===")
for mitglied in crew:
    print(f"  {mitglied[0]} | {mitglied[1]} | Sektor: {mitglied[2]}")

# Schritt 2: Neues Mitglied
crew.append(["Nav Zara", "Pilotin", "Delta"])
print(f"Crew-Stärke: {len(crew)}")

# Schritt 3: Sortieren nach Name
crew.sort(key=lambda m: m[0])
print("\n=== Alphabetisch ===")
for m in crew:
    print(f"  {m[0]}")
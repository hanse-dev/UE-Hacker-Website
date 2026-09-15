# Schritt 1: Gilden-Liste (verschachtelt: [Name, Level, Pferd])
gilde = [
    ["Lisa", 5, "Thunder"],
    ["Tom", 3, "Luna"],
    ["Sarah", 7, "Midnight"],
]
print("=== Reiter-Gilde ===")
for reiter in gilde:
    print(f"  {reiter[0]}, Level {reiter[1]}, Pferd: {reiter[2]}")

# Schritt 2: Neuen Reiter hinzufügen
gilde.append(["Max", 1, "Star"])
print(f"Mitglieder: {len(gilde)}")

# Schritt 3: Nach Level sortieren
gilde.sort(key=lambda r: r[1], reverse=True)
print("\n=== Rangliste ===")
for i, r in enumerate(gilde, 1):
    print(f"  {i}. {r[0]} (Level {r[1]})")
import random

# Schritt 1: Würfel-Orakel
wuerfe = [random.randint(1, 6) for _ in range(3)]
print("=== Würfel-Orakel ===")
print(f"Würfe: {wuerfe}")

# Schritt 2: Regal wählen
regale = ["Regal der Elemente", "Regal der Tiere", "Regal der Sterne", "Regal der Schatten", "Regal der Helden"]
gewaehltes_regal = random.choice(regale)
print(f"\nDein Regal: {gewaehltes_regal}")

# Schritt 3: Schriftrollen ziehen
schriftrollen = ["Rolle des Feuers", "Rolle des Windes", "Rolle der Sterne", "Rolle der Schatten", "Rolle der Erde", "Rolle des Eises"]
gezogen = random.sample(schriftrollen, 3)
print(f"\nGezogene Schriftrollen: {gezogen}")

# Schritt 4: Lesereihenfolge mischen
random.shuffle(gezogen)
print(f"Lesereihenfolge: {gezogen}")

# Bonus: Durchschnitt der Würfe
durchschnitt = round(sum(wuerfe) / len(wuerfe), 2)
print(f"\nDurchschnittswurf: {durchschnitt}")

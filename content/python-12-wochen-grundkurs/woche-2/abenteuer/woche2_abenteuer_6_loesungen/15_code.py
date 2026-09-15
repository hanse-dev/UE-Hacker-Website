# Schritt 1 – 🔥 Feuer befragen
name = input("Wie heißt du? ")

# Schritt 2 – 🪨 Erde befragen
alter = int(input("Wie alt bist du? "))

# Schritt 3 – 💧 Wasser befragen
zauberkraft = float(input("Deine Zauberkraft (z.B. 7.5)? "))

# Schritt 4 – 💨 Luft bestimmen
ist_maechtig = zauberkraft > 5.0

print(f"\n=== PROPHEZEIUNG FÜR {name.upper()} ===")
print(f"Alter: {alter} Jahre")
print(f"Zauberkraft: {zauberkraft}")
if ist_maechtig:
    print(f"{name}, deine Kraft übersteigt das gewöhnliche Maß!")
else:
    print(f"{name}, deine Kraft wird mit der Zeit wachsen.")

# Bonus: Elemente der Antworten
print(f"\nElement-Check:")
print(f"  Name:        {type(name)}")
print(f"  Alter:       {type(alter)}")
print(f"  Zauberkraft: {type(zauberkraft)}")
print(f"  Ist mächtig: {type(ist_maechtig)}")

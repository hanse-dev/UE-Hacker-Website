# Beispiel 2: Regale, Schriftrollen und Mischen
import random

regale = ["Regal der Elemente", "Regal der Tiere", "Regal der Sterne", "Regal der Schatten", "Regal der Helden"]
print(f"Alle Regale: {regale}")

# Ein zufälliges Regal
gewaehltes_regal = random.choice(regale)
print(f"Dein Regal: {gewaehltes_regal}")

# Drei verschiedene Schriftrollen ziehen (ohne Wiederholung!)
schriftrollen = random.sample(regale, 3)
print(f"Gezogene Schriftrollen: {schriftrollen}")

# Reihenfolge mischen
reihenfolge = regale.copy()
random.shuffle(reihenfolge)
print(f"Gemischte Lesereihenfolge: {reihenfolge}")

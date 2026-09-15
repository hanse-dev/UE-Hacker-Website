import random
import math

# Schritt 1: Pferdeauswahl
pferde_namen = ["Thunder", "Luna", "Blitz", "Silber", "Sturm", "Wolke"]
gewaehltes_pferd = random.choice(pferde_namen)
print("=== Reiterhof Sonnental ===")
print(f"Alle Pferde: {pferde_namen}")
print(f"Heutiges Tagespferd: {gewaehltes_pferd}")

# Schritt 2: Wetter-Simulation
print("\nWetter-Vorhersage (3 Tage):")
tage = ["Montag", "Dienstag", "Mittwoch"]
for tag in tage:
    temperatur = round(random.uniform(-10, 30), 1)
    print(f"  {tag}: {temperatur}°C")

# Schritt 3: Futter-Verbrauch
print("\nFutterplan:")
pferde_futter = ["Thunder", "Luna", "Blitz"]
gesamt_futter = 0
for pferd in pferde_futter:
    futter = random.randint(5, 15)
    gesamt_futter += futter
    print(f"  {pferd}: {futter} kg")
print(f"  Gesamt: {gesamt_futter} kg")

# Schritt 4: Pferde-Generator mit Geschwindigkeit
print("\nGeschwindigkeits-Rangliste:")
renn_pferde = [(name, random.randint(1, 10)) for name in ["Blitz", "Sturm", "Silber"]]
for name, geschwindigkeit in renn_pferde:
    print(f"  {name}: Geschwindigkeit {geschwindigkeit}/10")

# Bonus: Normalverteilung
futter_gauss = round(random.gauss(10, 2), 1)
print(f"\nBonus – Gauss-Futtermenge: {futter_gauss} kg")
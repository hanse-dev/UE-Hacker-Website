import random

# Schritt 1 – Flotten-Daten
flotte = [
    {"name": "Nebula-1", "klasse": "Kreuzer"},
    {"name": "Nebula-2", "klasse": "Fregatte"},
    {"name": "Nebula-3", "klasse": "Zerstörer"},
]

def beschreibe_flottenbewegung(schiff, ziel):
    return f"{schiff['name']} ({schiff['klasse']}) fliegt zu {ziel}."

# Schritt 2 – Effizienz-Funktion
def berechne_flotteneffizienz(formation):
    effizienz = {"Keil": 80, "Linie": 65, "Verteidigung": 90}
    return effizienz.get(formation, 50)

# Schritt 3 – Kommunikationsnetz prüfen
def kommunikation_stabil(entfernung_km):
    return entfernung_km <= 10000

# Schritt 4 – Flottenbericht
def erstelle_flottenbericht(flotte, effizienz):
    bericht = f"=== FLOTTENBERICHT ===\n"
    bericht += f"Schiffe: {len(flotte)}\n"
    for s in flotte:
        bericht += f"  {s['name']} – {s['klasse']}\n"
    bericht += f"Gesamteffizienz: {effizienz}%\n"
    return bericht

# Hauptteil
for s in flotte:
    print(beschreibe_flottenbewegung(s, "Sektor Gamma-7"))

formation = "Keil"
effizienz = berechne_flotteneffizienz(formation)
print(f"\nFormation: {formation} → Effizienz: {effizienz}%")

for distanz in [5000, 12000]:
    status = "stabil" if kommunikation_stabil(distanz) else "instabil"
    print(f"Kommunikation bei {distanz} km: {status}")

print()
print(erstelle_flottenbericht(flotte, effizienz))

# Bonus – Flottenvergleich
flotte_b_effizienz = berechne_flotteneffizienz("Linie")
print(f"Flotte A (Keil): {effizienz}% | Flotte B (Linie): {flotte_b_effizienz}%")
if effizienz >= flotte_b_effizienz:
    print("Flotte A hat höhere Gesamteffizienz.")
else:
    print("Flotte B hat höhere Gesamteffizienz.")
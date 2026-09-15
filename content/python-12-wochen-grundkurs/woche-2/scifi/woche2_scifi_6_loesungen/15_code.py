# Schritt 1 – Asteroiden katalogisieren
asteroid1_name = "Kepler-99A"
asteroid1_mineralgehalt = 5000
asteroid1_reinheit = 0.85
asteroid1_wert_pro_kg = 12.0

asteroid2_name = "Vega-17B"
asteroid2_mineralgehalt = 3500
asteroid2_reinheit = 0.97
asteroid2_wert_pro_kg = 18.5

# Schritt 2 – Rohwert berechnen
rohwert1 = asteroid1_mineralgehalt * asteroid1_reinheit * asteroid1_wert_pro_kg
rohwert2 = asteroid2_mineralgehalt * asteroid2_reinheit * asteroid2_wert_pro_kg

# Schritt 3 – Wertvergleich
print(f"{asteroid1_name}: Rohwert {rohwert1} Cyber Credits")
print(f"{asteroid2_name}: Rohwert {rohwert2} Cyber Credits")
print()

if rohwert1 > rohwert2:
    wertvoller = asteroid1_name
else:
    wertvoller = asteroid2_name

# Schritt 4 – Abbauentscheidung
print(f"Wertvoller Asteroid: {wertvoller} wird abgebaut!")
durchschnittswert = (rohwert1 + rohwert2) / 2
print(f"Durchschnittswert: {durchschnittswert:.2f} Cyber Credits")

# Bonus
mehrwert = abs(rohwert1 - rohwert2)
print(f"Wertunterschied: {mehrwert:.2f} Cyber Credits")
# Schritt 1 – Zauber erstellen
z1_name = "Phönixfeuer"
z1_staerke = 92.5
z1_komplexitaet = 5
z1_dauer = 8

z2_name = "Frosthauch"
z2_staerke = 68.0
z2_komplexitaet = 3
z2_dauer = 4

z3_name = "Donnerruf"
z3_staerke = 75.5
z3_komplexitaet = 4
z3_dauer = 6

z4_name = "Lichtsplitter"
z4_staerke = 55.0
z4_komplexitaet = 2
z4_dauer = 3

z5_name = "Schattenwelle"
z5_staerke = 83.0
z5_komplexitaet = 4
z5_dauer = 7

# Schritt 2 – Beschreibungen ausgeben
print("=== ZAUBERWERKSTATT-PROTOKOLL ===")
print(f"{z1_name}: Stärke {z1_staerke}, Komplexität {z1_komplexitaet}, Dauer {z1_dauer}s")
print(f"{z2_name}: Stärke {z2_staerke}, Komplexität {z2_komplexitaet}, Dauer {z2_dauer}s")
print(f"{z3_name}: Stärke {z3_staerke}, Komplexität {z3_komplexitaet}, Dauer {z3_dauer}s")
print(f"{z4_name}: Stärke {z4_staerke}, Komplexität {z4_komplexitaet}, Dauer {z4_dauer}s")
print(f"{z5_name}: Stärke {z5_staerke}, Komplexität {z5_komplexitaet}, Dauer {z5_dauer}s")
print()

# Schritt 3 – Komplexität summieren
gesamt_komplexitaet = z1_komplexitaet + z2_komplexitaet + z3_komplexitaet + z4_komplexitaet + z5_komplexitaet
print(f"Gesamtkomplexität: {gesamt_komplexitaet}")

# Schritt 4 – Stärkste und komplexeste Zauber
print(f"Stärkster Zauber: {z1_name} ({z1_staerke})")
print(f"Komplexester Zauber: {z1_name} (Komplexität {z1_komplexitaet})")

# Schritt 5 – Durchschnittstärke
gesamt_staerke = z1_staerke + z2_staerke + z3_staerke + z4_staerke + z5_staerke
durchschnitt_staerke = gesamt_staerke / 5
print(f"Durchschnittsstärke: {durchschnitt_staerke}")

# Schritt 6 – Mächtige filtern (Boolean)
z1_ueber_durchschnitt = z1_staerke > durchschnitt_staerke
z2_ueber_durchschnitt = z2_staerke > durchschnitt_staerke
z3_ueber_durchschnitt = z3_staerke > durchschnitt_staerke
z4_ueber_durchschnitt = z4_staerke > durchschnitt_staerke
z5_ueber_durchschnitt = z5_staerke > durchschnitt_staerke
print(f"{z1_name} über Durchschnitt: {z1_ueber_durchschnitt}")
print(f"{z2_name} über Durchschnitt: {z2_ueber_durchschnitt}")
print(f"{z3_name} über Durchschnitt: {z3_ueber_durchschnitt}")
print(f"{z4_name} über Durchschnitt: {z4_ueber_durchschnitt}")
print(f"{z5_name} über Durchschnitt: {z5_ueber_durchschnitt}")

# Bonus: Effizienz
print()
print(f"Effizienz {z1_name}: {z1_staerke / z1_komplexitaet:.2f}")
print(f"Effizienz {z2_name}: {z2_staerke / z2_komplexitaet:.2f}")
print(f"Effizienz {z3_name}: {z3_staerke / z3_komplexitaet:.2f}")
print(f"Effizienz {z4_name}: {z4_staerke / z4_komplexitaet:.2f}")
print(f"Effizienz {z5_name}: {z5_staerke / z5_komplexitaet:.2f}")

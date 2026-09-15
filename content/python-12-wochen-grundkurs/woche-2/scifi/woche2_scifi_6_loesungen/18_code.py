# Schritt 1 – Flotte erfassen (8 Schiffe)
s1_name = "ISS Aurora"
s1_energie = 87
s2_name = "ISS Titan"
s2_energie = 43
s3_name = "ISS Nova"
s3_energie = 96
s4_name = "ISS Pulsar"
s4_energie = 61
s5_name = "ISS Quasar"
s5_energie = 78
s6_name = "ISS Nebula"
s6_energie = 34
s7_name = "ISS Comet"
s7_energie = 55
s8_name = "ISS Vortex"
s8_energie = 92

# Schritt 2 – Statusprotokoll
print("=== DOCK-PROTOKOLL ===")
print(f"{s1_name}: Energie {s1_energie}%")
print(f"{s2_name}: Energie {s2_energie}%")
print(f"{s3_name}: Energie {s3_energie}%")
print(f"{s4_name}: Energie {s4_energie}%")
print(f"{s5_name}: Energie {s5_energie}%")
print(f"{s6_name}: Energie {s6_energie}%")
print(f"{s7_name}: Energie {s7_energie}%")
print(f"{s8_name}: Energie {s8_energie}%")
print()

# Schritt 3 – Durchschnitt
gesamt_energie = s1_energie + s2_energie + s3_energie + s4_energie + s5_energie + s6_energie + s7_energie + s8_energie
durchschnitt = gesamt_energie / 8
print(f"Durchschnittsenergie: {durchschnitt}%")

# Schritt 4 – Bestes Schiff
print(f"Bestes Schiff: {s3_name} mit {s3_energie}% Energie")

# Schritt 5 – Energiebedarf
anzahl_schiffe = 8
gesamt_energiebedarf = anzahl_schiffe * 100
print(f"Gesamt-Energiebedarf (100% pro Schiff): {gesamt_energiebedarf} Einheiten")

# Bonus
unter_durchschnitt = 0
if s1_energie < durchschnitt: unter_durchschnitt += 1
if s2_energie < durchschnitt: unter_durchschnitt += 1
if s3_energie < durchschnitt: unter_durchschnitt += 1
if s4_energie < durchschnitt: unter_durchschnitt += 1
if s5_energie < durchschnitt: unter_durchschnitt += 1
if s6_energie < durchschnitt: unter_durchschnitt += 1
if s7_energie < durchschnitt: unter_durchschnitt += 1
if s8_energie < durchschnitt: unter_durchschnitt += 1
print(f"Schiffe unter Durchschnitt: {unter_durchschnitt}")
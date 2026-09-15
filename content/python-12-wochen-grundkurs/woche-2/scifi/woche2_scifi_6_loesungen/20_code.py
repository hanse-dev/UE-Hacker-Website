# Schritt 1 – KI-Modelle erstellen (5 Modelle)
ki1_name = "ARIA-7"
ki1_genauigkeit = 0.94
ki1_parameter = 7000000
ki1_trainingszeit = 48

ki2_name = "NEXUS-3"
ki2_genauigkeit = 0.87
ki2_parameter = 2500000
ki2_trainingszeit = 24

ki3_name = "QUANTUM-1"
ki3_genauigkeit = 0.98
ki3_parameter = 15000000
ki3_trainingszeit = 96

ki4_name = "DELTA-9"
ki4_genauigkeit = 0.79
ki4_parameter = 1200000
ki4_trainingszeit = 12

ki5_name = "SIGMA-X"
ki5_genauigkeit = 0.91
ki5_parameter = 5000000
ki5_trainingszeit = 36

# Schritt 2 – Modellbeschreibungen
print("=== KI-LABOR-PROTOKOLL ===")
print(f"{ki1_name}: Genauigkeit {ki1_genauigkeit}, Parameter {ki1_parameter}, Training {ki1_trainingszeit}h")
print(f"{ki2_name}: Genauigkeit {ki2_genauigkeit}, Parameter {ki2_parameter}, Training {ki2_trainingszeit}h")
print(f"{ki3_name}: Genauigkeit {ki3_genauigkeit}, Parameter {ki3_parameter}, Training {ki3_trainingszeit}h")
print(f"{ki4_name}: Genauigkeit {ki4_genauigkeit}, Parameter {ki4_parameter}, Training {ki4_trainingszeit}h")
print(f"{ki5_name}: Genauigkeit {ki5_genauigkeit}, Parameter {ki5_parameter}, Training {ki5_trainingszeit}h")
print()

# Schritt 3 – Parameter summieren
gesamt_parameter = ki1_parameter + ki2_parameter + ki3_parameter + ki4_parameter + ki5_parameter
print(f"Gesamtparameter: {gesamt_parameter}")

# Schritt 4 – Bestes und größtes Modell
print(f"Genauestes Modell: {ki3_name} ({ki3_genauigkeit})")
print(f"Größtes Modell: {ki3_name} ({ki3_parameter} Parameter)")

# Schritt 5 – Durchschnittsgenauigkeit
gesamt_genauigkeit = ki1_genauigkeit + ki2_genauigkeit + ki3_genauigkeit + ki4_genauigkeit + ki5_genauigkeit
durchschnitt = gesamt_genauigkeit / 5
print(f"Durchschnittsgenauigkeit: {durchschnitt:.3f}")

# Schritt 6 – Leistungsstarke filtern
ki1_stark = ki1_genauigkeit > durchschnitt
ki2_stark = ki2_genauigkeit > durchschnitt
ki3_stark = ki3_genauigkeit > durchschnitt
ki4_stark = ki4_genauigkeit > durchschnitt
ki5_stark = ki5_genauigkeit > durchschnitt
print(f"{ki1_name} über Durchschnitt: {ki1_stark}")
print(f"{ki2_name} über Durchschnitt: {ki2_stark}")
print(f"{ki3_name} über Durchschnitt: {ki3_stark}")
print(f"{ki4_name} über Durchschnitt: {ki4_stark}")
print(f"{ki5_name} über Durchschnitt: {ki5_stark}")

# Bonus: Effizienz
print()
print(f"Effizienz {ki1_name}: {ki1_genauigkeit / ki1_parameter * 1000000:.4f}")
print(f"Effizienz {ki2_name}: {ki2_genauigkeit / ki2_parameter * 1000000:.4f}")
print(f"Effizienz {ki3_name}: {ki3_genauigkeit / ki3_parameter * 1000000:.4f}")
print(f"Effizienz {ki4_name}: {ki4_genauigkeit / ki4_parameter * 1000000:.4f}")
print(f"Effizienz {ki5_name}: {ki5_genauigkeit / ki5_parameter * 1000000:.4f}")
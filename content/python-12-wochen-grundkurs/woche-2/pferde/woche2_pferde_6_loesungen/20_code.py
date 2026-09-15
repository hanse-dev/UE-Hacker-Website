# Schritt 1 – Übungen erstellen (5 Übungen)
u1_name = "Dressur-Grundgangarten"
u1_intensitaet = 2.5
u1_dauer = 20
u1_schwierigkeit = 2

u2_name = "Springparcours"
u2_intensitaet = 4.5
u2_dauer = 30
u2_schwierigkeit = 5

u3_name = "Geländeritt"
u3_intensitaet = 3.8
u3_dauer = 45
u3_schwierigkeit = 4

u4_name = "Longierstunde"
u4_intensitaet = 2.0
u4_dauer = 25
u4_schwierigkeit = 2

u5_name = "Hindernisarbeit"
u5_intensitaet = 3.5
u5_dauer = 35
u5_schwierigkeit = 4

# Schritt 2 – Übungsbeschreibungen
print("=== TRAININGSHALLE-PROTOKOLL ===")
print(f"{u1_name}: Intensität {u1_intensitaet}, Dauer {u1_dauer} Min, Schwierigkeit {u1_schwierigkeit}")
print(f"{u2_name}: Intensität {u2_intensitaet}, Dauer {u2_dauer} Min, Schwierigkeit {u2_schwierigkeit}")
print(f"{u3_name}: Intensität {u3_intensitaet}, Dauer {u3_dauer} Min, Schwierigkeit {u3_schwierigkeit}")
print(f"{u4_name}: Intensität {u4_intensitaet}, Dauer {u4_dauer} Min, Schwierigkeit {u4_schwierigkeit}")
print(f"{u5_name}: Intensität {u5_intensitaet}, Dauer {u5_dauer} Min, Schwierigkeit {u5_schwierigkeit}")
print()

# Schritt 3 – Gesamtdauer
gesamt_dauer = u1_dauer + u2_dauer + u3_dauer + u4_dauer + u5_dauer
print(f"Gesamtdauer: {gesamt_dauer} Minuten")

# Schritt 4 – Intensivste und schwierigste Übung
print(f"Intensivste Übung: {u2_name} ({u2_intensitaet})")
print(f"Schwierigste Übung: {u2_name} (Schwierigkeit {u2_schwierigkeit})")

# Schritt 5 – Durchschnittsintensität
gesamt_intensitaet = u1_intensitaet + u2_intensitaet + u3_intensitaet + u4_intensitaet + u5_intensitaet
durchschnitt = gesamt_intensitaet / 5
print(f"Durchschnittsintensität: {durchschnitt}")

# Schritt 6 – Boolean-Markierung
u1_anspruchsvoll = u1_intensitaet > durchschnitt
u2_anspruchsvoll = u2_intensitaet > durchschnitt
u3_anspruchsvoll = u3_intensitaet > durchschnitt
u4_anspruchsvoll = u4_intensitaet > durchschnitt
u5_anspruchsvoll = u5_intensitaet > durchschnitt
print(f"{u1_name} über Durchschnitt: {u1_anspruchsvoll}")
print(f"{u2_name} über Durchschnitt: {u2_anspruchsvoll}")
print(f"{u3_name} über Durchschnitt: {u3_anspruchsvoll}")
print(f"{u4_name} über Durchschnitt: {u4_anspruchsvoll}")
print(f"{u5_name} über Durchschnitt: {u5_anspruchsvoll}")

# Bonus: Effizienz
print()
print(f"Effizienz {u1_name}: {u1_intensitaet / u1_dauer * 10:.2f}")
print(f"Effizienz {u2_name}: {u2_intensitaet / u2_dauer * 10:.2f}")
print(f"Effizienz {u3_name}: {u3_intensitaet / u3_dauer * 10:.2f}")
print(f"Effizienz {u4_name}: {u4_intensitaet / u4_dauer * 10:.2f}")
print(f"Effizienz {u5_name}: {u5_intensitaet / u5_dauer * 10:.2f}")
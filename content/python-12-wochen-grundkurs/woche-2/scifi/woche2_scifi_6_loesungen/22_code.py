# Schritt 1 – Missionen definieren
m1_ziel = "Alpha Centauri Sonde platzieren"
m1_dauer = 180
m1_kosten = 85000000
m1_crew = 12
m1_erfolg = 0.75

m2_ziel = "Mondstation erweitern"
m2_dauer = 30
m2_kosten = 25000000
m2_crew = 6
m2_erfolg = 0.95

# Schritt 2 – Missionsprotokoll
print("=== MISSIONS-PROTOKOLL ===")
print(f"Mission 1: {m1_ziel}")
print(f"  Dauer: {m1_dauer} Tage, Kosten: {m1_kosten} CC, Crew: {m1_crew}, Erfolg: {m1_erfolg * 100}%")
print(f"Mission 2: {m2_ziel}")
print(f"  Dauer: {m2_dauer} Tage, Kosten: {m2_kosten} CC, Crew: {m2_crew}, Erfolg: {m2_erfolg * 100}%")
print()

# Schritt 3 – Gesamtwerte
gesamt_kosten = m1_kosten + m2_kosten
gesamt_crew = m1_crew + m2_crew
print(f"Gesamtkosten: {gesamt_kosten} CC")
print(f"Gesamt-Crew: {gesamt_crew} Personen")
print()

# Schritt 4 – Erfolg prognostizieren
erw_erfolg1 = m1_kosten * m1_erfolg
erw_erfolg2 = m2_kosten * m2_erfolg
print(f"Erwartete Investitionsrendite M1: {erw_erfolg1:.0f} CC")
print(f"Erwartete Investitionsrendite M2: {erw_erfolg2:.0f} CC")
print()

# Schritt 5 – Missionen vergleichen
print(f"Kostenunterschied: {m1_kosten - m2_kosten} CC")
print(f"Dauerunterschied: {m1_dauer - m2_dauer} Tage")
print(f"Erfolgsunterschied: {(m2_erfolg - m1_erfolg) * 100}%")

# Schritt 6 – Profitabilität
m2_profitabler = erw_erfolg2 > erw_erfolg1
print(f"Mission 2 profitabler: {m2_profitabler}")

# Bonus: Kosten pro Crewmitglied
print()
print(f"Kosten pro Crew-Mitglied M1: {m1_kosten / m1_crew:.0f} CC")
print(f"Kosten pro Crew-Mitglied M2: {m2_kosten / m2_crew:.0f} CC")

print()
print("🎉 Finale Herausforderung abgeschlossen!")
print("🏆 Du hast den Shapeshifter der instabilen Daten besiegt!")
print("⭐ Titel erhalten: Meister der Quanten-Typen")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 2 gemeistert!")
print("🚀 Nächste Woche: Bedingungen (if-else)!")
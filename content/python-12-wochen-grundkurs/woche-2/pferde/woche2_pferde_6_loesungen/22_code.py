# Schritt 1 – Trainingseinheiten definieren
e1_ziel = "Dressur-Prüfung Klasse A"
e1_dauer = 5
e1_kosten = 350
e1_teilnehmer = 8
e1_erfolg = 0.85

e2_ziel = "Springturnier Vorbereitung"
e2_dauer = 3
e2_kosten = 200
e2_teilnehmer = 5
e2_erfolg = 0.90

# Schritt 2 – Trainingsprotokoll
print("=== TRAININGSPROTOKOLL ===")
print(f"Einheit 1: {e1_ziel}")
print(f"  Dauer: {e1_dauer} Tage, Kosten: {e1_kosten} €, Teilnehmer: {e1_teilnehmer}, Erfolg: {e1_erfolg * 100}%")
print(f"Einheit 2: {e2_ziel}")
print(f"  Dauer: {e2_dauer} Tage, Kosten: {e2_kosten} €, Teilnehmer: {e2_teilnehmer}, Erfolg: {e2_erfolg * 100}%")
print()

# Schritt 3 – Gesamtwerte
gesamt_kosten = e1_kosten + e2_kosten
gesamt_teilnehmer = e1_teilnehmer + e2_teilnehmer
print(f"Gesamtkosten: {gesamt_kosten} €")
print(f"Gesamt-Teilnehmer: {gesamt_teilnehmer}")
print()

# Schritt 4 – Erfolg prognostizieren
erwarteter_erfolg1 = e1_teilnehmer * e1_erfolg
erwarteter_erfolg2 = e2_teilnehmer * e2_erfolg
print(f"Erwartete erfolgreiche Teilnehmer E1: {erwarteter_erfolg1}")
print(f"Erwartete erfolgreiche Teilnehmer E2: {erwarteter_erfolg2}")
print()

# Schritt 5 – Einheiten vergleichen
print(f"Kostenunterschied: {e1_kosten - e2_kosten} €")
print(f"Dauerunterschied: {e1_dauer - e2_dauer} Tage")
print(f"Erfolgsunterschied: {(e2_erfolg - e1_erfolg) * 100}%")

# Schritt 6 – Effizienz
e1_effizienter = (e1_kosten / e1_teilnehmer) < (e2_kosten / e2_teilnehmer)
print(f"Einheit 1 kosteneffizienter: {e1_effizienter}")

# Bonus: Kosten pro Teilnehmer
print()
print(f"Kosten pro Teilnehmer E1: {e1_kosten / e1_teilnehmer:.2f} €")
print(f"Kosten pro Teilnehmer E2: {e2_kosten / e2_teilnehmer:.2f} €")

print()
print("🎉 Abschluss-Challenge abgeschlossen!")
print("🏆 Du hast das Dressurpferd der widerspenstigen Hufe gemeistert!")
print("⭐ Titel erhalten: Meister der Hufschlag-Typen")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 2 gemeistert!")
print("🐴 Nächste Woche: Bedingungen (if-else)!")
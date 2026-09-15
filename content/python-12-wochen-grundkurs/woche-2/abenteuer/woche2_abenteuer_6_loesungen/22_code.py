# Schritt 1 – Quests definieren
q1_ziel = "Drachenhöhle säubern"
q1_dauer = 7
q1_belohnung = 1200
q1_gruppengroesse = 5
q1_erfolg = 0.8

q2_ziel = "Verlorene Relikte bergen"
q2_dauer = 3
q2_belohnung = 600
q2_gruppengroesse = 3
q2_erfolg = 0.95

# Schritt 2 – Questprotokoll
print("=== QUEST-PROTOKOLL ===")
print(f"Quest 1: {q1_ziel}")
print(f"  Dauer: {q1_dauer} Tage, Belohnung: {q1_belohnung} Gold, Gruppe: {q1_gruppengroesse}, Erfolg: {q1_erfolg * 100}%")
print(f"Quest 2: {q2_ziel}")
print(f"  Dauer: {q2_dauer} Tage, Belohnung: {q2_belohnung} Gold, Gruppe: {q2_gruppengroesse}, Erfolg: {q2_erfolg * 100}%")
print()

# Schritt 3 – Gesamtwerte
gesamt_belohnung = q1_belohnung + q2_belohnung
gesamt_gruppe = q1_gruppengroesse + q2_gruppengroesse
print(f"Gesamtbelohnung: {gesamt_belohnung} Gold")
print(f"Gesamt-Gruppengröße: {gesamt_gruppe} Personen")
print()

# Schritt 4 – Erfolg prognostizieren
erwartete_belohnung1 = q1_belohnung * q1_erfolg
erwartete_belohnung2 = q2_belohnung * q2_erfolg
print(f"Erwartete Belohnung Quest 1: {erwartete_belohnung1} Gold")
print(f"Erwartete Belohnung Quest 2: {erwartete_belohnung2} Gold")
print()

# Schritt 5 – Quests vergleichen
print(f"Belohnungsunterschied: {q1_belohnung - q2_belohnung} Gold")
print(f"Dauerunterschied: {q1_dauer - q2_dauer} Tage")
print(f"Erfolgsunterschied: {(q2_erfolg - q1_erfolg) * 100}%")

# Schritt 6 – Rentabilität
q1_rentabel = erwartete_belohnung1 > erwartete_belohnung2
print(f"Quest 1 rentabler: {q1_rentabel}")

# Bonus: Belohnung pro Gruppenmitglied
print()
print(f"Belohnung pro Person Quest 1: {q1_belohnung / q1_gruppengroesse} Gold")
print(f"Belohnung pro Person Quest 2: {q2_belohnung / q2_gruppengroesse} Gold")

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Golem der verwirrten Formen besiegt!")
print("⭐ Die Turmwächterin nickt: Meister der vier Elemente!")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 2 gemeistert!")
print("📚 Nächste Woche: Bedingungen (if-else)!")

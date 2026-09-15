# Schritt 1 – Pferde erfassen
pferd1_name = "Donnerwolke"
pferd1_alter = 8
pferd1_dressur = 88
pferd1_spring = 92

pferd2_name = "Silberwind"
pferd2_alter = 6
pferd2_dressur = 95
pferd2_spring = 79

# Schritt 2 – Gesamtpunkte berechnen
gesamt1 = pferd1_dressur + pferd1_spring
gesamt2 = pferd2_dressur + pferd2_spring

# Schritt 3 – Sieger bestimmen
print(f"{pferd1_name} (Alter {pferd1_alter}): {gesamt1} Punkte")
print(f"{pferd2_name} (Alter {pferd2_alter}): {gesamt2} Punkte")
print()

if gesamt1 > gesamt2:
    sieger = pferd1_name
else:
    sieger = pferd2_name

# Schritt 4 – Siegesmeldung
print(f"Das Turnier gewinnt: {sieger}!")
durchschnitt_punkte = (gesamt1 + gesamt2) / 2
print(f"Durchschnittliche Punktzahl: {durchschnitt_punkte}")

# Bonus
vorsprung = abs(gesamt1 - gesamt2)
print(f"Vorsprung des Siegers: {vorsprung} Punkte")
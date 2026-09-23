gilde = [["Aria", "Magierin", 15], ["Thorin", "Krieger", 12], ["Luna", "Schurkin", 8]]
gilde.append(["Finn", "Bogenschütze", 10])
gesamt = 0
for mitglied in gilde:
    gesamt += mitglied[2]
print(f"Mitglieder: {len(gilde)}")
print(f"Gesamtlevel: {gesamt}")

gilde = [["Anna", "Springen", 15], ["Ben", "Dressur", 12], ["Clara", "Voltigieren", 8]]
gilde.append(["David", "Western", 10])
gesamt = 0
for mitglied in gilde:
    gesamt += mitglied[2]
print(f"Mitglieder: {len(gilde)}")
print(f"Gesamtlevel: {gesamt}")

reitgruppe = [["Anna", "Springen", 15], ["Ben", "Dressur", 12], ["Clara", "Voltigieren", 8]]
reitgruppe.append(["David", "Western", 10])
gesamt = 0
for mitglied in reitgruppe:
    gesamt += mitglied[2]
print(f"Mitglieder: {len(reitgruppe)}")
print(f"Gesamtlevel: {gesamt}")

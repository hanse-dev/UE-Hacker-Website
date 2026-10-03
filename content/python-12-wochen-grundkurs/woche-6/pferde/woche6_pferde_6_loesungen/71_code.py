reitgruppe = [["Anna", "Springen", 15], ["Ben", "Dressur", 12], ["Clara", "Voltigieren", 8]]
reitgruppe.append(["David", "Western", 10])
staerkster = reitgruppe[0]
for mitglied in reitgruppe:
    if mitglied[2] > staerkster[2]:
        staerkster = mitglied
print(f"Stärkster: {staerkster[0]}")

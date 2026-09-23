gilde = [["Anna", "Springen", 15], ["Ben", "Dressur", 12], ["Clara", "Voltigieren", 8]]
gilde.append(["David", "Western", 10])
staerkster = gilde[0]
for mitglied in gilde:
    if mitglied[2] > staerkster[2]:
        staerkster = mitglied
print(f"Stärkster: {staerkster[0]}")

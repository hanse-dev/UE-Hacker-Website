gilde = [["Nova", "Pilotin", 15], ["Kira", "Technikerin", 12], ["Juno", "Ärztin", 8]]
gilde.append(["Rex", "Ingenieur", 10])
staerkster = gilde[0]
for mitglied in gilde:
    if mitglied[2] > staerkster[2]:
        staerkster = mitglied
print(f"Stärkster: {staerkster[0]}")

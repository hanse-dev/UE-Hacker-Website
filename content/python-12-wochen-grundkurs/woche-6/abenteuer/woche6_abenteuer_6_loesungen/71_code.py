gilde = [["Aria", "Magierin", 15], ["Thorin", "Krieger", 12], ["Luna", "Schurkin", 8]]
gilde.append(["Finn", "Bogenschütze", 10])
staerkster = gilde[0]
for mitglied in gilde:
    if mitglied[2] > staerkster[2]:
        staerkster = mitglied
print(f"Stärkster: {staerkster[0]}")

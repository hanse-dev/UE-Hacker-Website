crew = [["Nova", "Pilotin", 15], ["Kira", "Technikerin", 12], ["Juno", "Ärztin", 8]]
crew.append(["Rex", "Ingenieur", 10])
staerkster = crew[0]
for mitglied in crew:
    if mitglied[2] > staerkster[2]:
        staerkster = mitglied
print(f"Stärkster: {staerkster[0]}")

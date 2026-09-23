gilde = [["Nova", "Pilotin", 15], ["Kira", "Technikerin", 12], ["Juno", "Ärztin", 8]]
gilde.append(["Rex", "Ingenieur", 10])
gesamt = 0
for mitglied in gilde:
    gesamt += mitglied[2]
print(f"Mitglieder: {len(gilde)}")
print(f"Gesamtlevel: {gesamt}")

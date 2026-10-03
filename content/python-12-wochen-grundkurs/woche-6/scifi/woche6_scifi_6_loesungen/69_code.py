crew = [["Nova", "Pilotin", 15], ["Kira", "Technikerin", 12], ["Juno", "Ärztin", 8]]
crew.append(["Rex", "Ingenieur", 10])
gesamt = 0
for mitglied in crew:
    gesamt += mitglied[2]
print(f"Mitglieder: {len(crew)}")
print(f"Gesamtlevel: {gesamt}")

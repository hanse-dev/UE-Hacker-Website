# Beispiel 3: Listen in Listen (verschachtelte Listen)
crew_mitglieder = [
    ["Captain Alex", "Kommandant", 35, "Alpha-Quadrant"],
    ["Dr. Zara", "Wissenschaftlerin", 28, "Beta-Quadrant"],
    ["Lt. Nova", "Pilotin", 26, "Gamma-Sektor"]
]

print("=== Crew-Mitglieder ===")
print(f"Erster Crew-Mitglied: {crew_mitglieder[0]}")
print(f"Name des ersten: {crew_mitglieder[0][0]}")
print(f"Position des zweiten: {crew_mitglieder[1][1]}")
print(f"Alter des dritten: {crew_mitglieder[2][2]} Jahre")
print(f"Sektor des ersten: {crew_mitglieder[0][3]}")
# Beispiel 3: Listen in Listen (verschachtelte Listen)
pferde_party = [
    ["Thunder", "Hannoveraner", 8, "Springen"],
    ["Luna", "Isländer", 5, "Dressur"],
    ["Storm", "Quarter Horse", 6, "Western"]
]

print("=== Pferde-Party ===")
print(f"Erstes Pferd: {pferde_party[0]}")
print(f"Name des ersten Pferdes: {pferde_party[0][0]}")
print(f"Rasse des zweiten Pferdes: {pferde_party[1][1]}")
print(f"Alter des dritten Pferdes: {pferde_party[2][2]} Jahre")
print(f"Disziplin des ersten Pferdes: {pferde_party[0][3]}")
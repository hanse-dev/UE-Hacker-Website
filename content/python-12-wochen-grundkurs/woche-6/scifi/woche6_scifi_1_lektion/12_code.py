# Beispiel 2: Listen sortieren
prioritaeten = [5, 2, 8, 1, 9, 3]
sektoren = ["Zeta", "Alpha", "Gamma", "Beta", "Delta"]

print("=== Listen sortieren ===")
print(f"Original-Prioritäten: {prioritaeten}")
print(f"Original-Sektoren: {sektoren}")

# Mit sort() direkt sortieren
prioritaeten.sort()
print(f"Prioritäten nach sort(): {prioritaeten}")

# Mit sorted() Kopie sortieren
sortierte_sektoren = sorted(sektoren)
print(f"Sektoren Original: {sektoren}")
print(f"Sektoren sortiert: {sortierte_sektoren}")

# Umgekehrt sortieren
prioritaeten.sort(reverse=True)
print(f"Prioritäten absteigend: {prioritaeten}")

# Mit reverse() Reihenfolge umkehren
sektoren.reverse()
print(f"Sektoren umgekehrt: {sektoren}")
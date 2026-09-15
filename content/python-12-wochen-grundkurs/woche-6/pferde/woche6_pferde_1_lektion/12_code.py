# Beispiel 2: Listen sortieren
level = [5, 2, 8, 1, 9, 3]
namen = ["Zara", "Anna", "Max", "Berta", "Klaus"]

print("=== Listen sortieren ===")
print(f"Original-Level: {level}")
print(f"Original-Namen: {namen}")

# Mit sort() direkt sortieren
level.sort()
print(f"Level nach sort(): {level}")

# Mit sorted() Kopie sortieren
sortierte_namen = sorted(namen)
print(f"Namen Original: {namen}")
print(f"Namen sortiert: {sortierte_namen}")

# Umgekehrt sortieren
level.sort(reverse=True)
print(f"Level absteigend: {level}")

# Mit reverse() Reihenfolge umkehren
namen.reverse()
print(f"Namen umgekehrt: {namen}")
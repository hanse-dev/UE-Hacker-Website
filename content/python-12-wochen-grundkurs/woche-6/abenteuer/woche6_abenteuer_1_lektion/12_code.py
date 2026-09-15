# Beispiel 2: Listen sortieren
zahlen = [5, 2, 8, 1, 9, 3]
namen = ["Zara", "Anna", "Max", "Berta", "Klaus"]

print("=== Listen sortieren ===")
print(f"Original-Zahlen: {zahlen}")
print(f"Original-Namen: {namen}")

# Mit sort() direkt sortieren
zahlen.sort()
print(f"Zahlen nach sort(): {zahlen}")

# Mit sorted() Kopie sortieren
sortierte_namen = sorted(namen)
print(f"Namen Original: {namen}")
print(f"Namen sortiert: {sortierte_namen}")

# Umgekehrt sortieren
zahlen.sort(reverse=True)
print(f"Zahlen absteigend: {zahlen}")

# Mit reverse() Reihenfolge umkehren
namen.reverse()
print(f"Namen umgekehrt: {namen}")
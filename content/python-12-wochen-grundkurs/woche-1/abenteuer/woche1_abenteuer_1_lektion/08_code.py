# Beispiel 1: Einfache Kombination
name = "Legolas"
waffe = "Bogen"
print("Held: " + name)
print("Waffe: " + waffe)

# Beispiel 2: Mit Zahlen (str() nötig!)
pfeile = 20
print("Pfeile: " + str(pfeile))

# Beispiel 3: Komplexe Sätze
print(name + " hat einen " + waffe + " mit " + str(pfeile) + " Pfeilen.")

# Beispiel 4: Mehrere Informationen
print()
print("=== CHARAKTERBOGEN ===")
print("Name: " + name)
print("Waffe: " + waffe)
print("Munition: " + str(pfeile) + " Pfeile")
print("=====================")
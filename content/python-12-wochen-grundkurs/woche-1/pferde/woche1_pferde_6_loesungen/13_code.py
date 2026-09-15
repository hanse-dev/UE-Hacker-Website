# Schritt 1 – Futterdaten erfassen
pferdename = "Comet"
futterart = "Hafer"
menge_kg = 5

# Schritt 2 – Fütterplan ausgeben
print("=== FÜTTERPLAN ===")
print("Pferd: " + pferdename)
print("Futter: " + futterart)
print("Menge: " + str(menge_kg) + " kg")

# Schritt 3 – Fütterungsbericht
print()
print(pferdename + " bekommt heute " + str(menge_kg) + " kg " + futterart + ".")
print("=== FÜTTERUNG ABGESCHLOSSEN ===")
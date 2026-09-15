# Beispiel 3: For-Schleife mit Schrittweite
print("=== Beispiel 3: Jede zweite Hürde ===")
# range(0, 11, 2) erzeugt: 0, 2, 4, 6, 8, 10
for hurde in range(0, 11, 2):
    print(f"Hürde {hurde}: Gesprungen!")

print("\n=== Die Schrittweite ===")
print("range(start, ende, schritt) überspringt Hürden")
print("Hier: jede zweite Hürde überspringen")
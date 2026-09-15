# Beispiel 2: For-Schleife mit Start und Ende
print("=== Beispiel 2: Zählen von 3 bis 7 ===")
# range(3, 8) erzeugt die Zahlen 3, 4, 5, 6, 7 (8 ist exklusiv!)
for zahl in range(3, 8):
    print(f"Zahl: {zahl}")

print("\n=== Wichtige Beobachtung ===")
print("range(start, ende) enthält start, aber nicht ende!")
print("Das ist wie bei Slices: [start:ende] ist ende-exklusiv")
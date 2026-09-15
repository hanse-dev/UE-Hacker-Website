# Beispiel 2: For-Schleife mit Start und Ende
print("=== Beispiel 2: Sektoren 3 bis 7 scannen ===")
# range(3, 8) erzeugt die Zahlen 3, 4, 5, 6, 7 (8 ist exklusiv!)
for sektor in range(3, 8):
    print(f"Sektor {sektor}: Scan abgeschlossen")

print("\n=== Wichtige Beobachtung ===")
print("range(start, ende) enthält start, aber nicht ende!")
print("Wie bei Koordinaten: von 3 bis VOR 8")
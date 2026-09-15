# Beispiel 2: For-Schleife mit Start und Ende
print("=== Beispiel 2: Hürden von 3 bis 7 ===")
# range(3, 8) erzeugt die Zahlen 3, 4, 5, 6, 7 (8 ist exklusiv!)
for hurde in range(3, 8):
    print(f"Hürde {hurde}: Sprung!")

print("\n=== Wichtige Beobachtung ===")
print("range(start, ende) enthält start, aber nicht ende!")
print("Wie bei einem Reitplatz: von 3 bis VOR 8")
anzahl = 0
for i in range(5):
    hoehe = 90 + i * 10
    
    if hoehe > 100:
        anzahl += 1
print(f"Höher als 100 cm: {anzahl}")

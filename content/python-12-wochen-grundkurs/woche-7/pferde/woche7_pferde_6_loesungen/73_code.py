def berechne_pausen(hindernis_anzahl):
    return (hindernis_anzahl + 1) // 2

print(f"Pausen: {berechne_pausen(5)}")
print(f"Pausen: {berechne_pausen(4)}")
print(f"Pausen: {berechne_pausen(0)}")

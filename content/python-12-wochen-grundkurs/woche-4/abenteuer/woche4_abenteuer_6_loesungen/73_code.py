zeile = 0
spalte = 0
zuege = 0
while zeile < 7:
    zeile += 1
    spalte += 1
    zuege += 1
if zeile == 7 and spalte == 7:
    print(f"Ziel erreicht nach {zuege} Zügen")

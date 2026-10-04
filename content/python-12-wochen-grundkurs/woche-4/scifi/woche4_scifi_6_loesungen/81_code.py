beste_distanz = 0
for verbrauch in range(10, 31, 10):
    treibstoff = 100
    schild = 60
    distanz = 0
    while treibstoff > 0 and schild > 0:
        distanz += 1
        treibstoff -= verbrauch
        schild -= 8
    if distanz > beste_distanz:
        beste_distanz = distanz
print(f"Beste Distanz: {beste_distanz}")

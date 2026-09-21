treibstoff = 100
schild = 60
distanz = 0
while treibstoff > 0 and schild > 0:
    distanz += 1
    treibstoff -= 20
    schild -= 8
    print(f"Portal {distanz}: Treibstoff {treibstoff}, Schild {schild}")

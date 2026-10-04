treibstoff = 100
schild = 60
distanz = 0
while treibstoff > 0 and schild > 0:
    distanz += 1
    treibstoff -= 20
    schild -= 8
print(f"Tunnel endete nach {distanz} Portalen")
if treibstoff <= 0:
    print("Grund: Treibstoff leer")

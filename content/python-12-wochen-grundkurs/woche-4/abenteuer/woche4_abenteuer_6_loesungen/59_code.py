position = 0
schritte = 0
while position < 50 and schritte < 10:
    position += 3
    schritte += 1
if position < 50:
    print(f"Verloren im Labyrinth nach {schritte} Schritten")

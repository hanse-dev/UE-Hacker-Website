leben = 100
mana = 50
tiefe = 0
while leben > 0 and mana > 0:
    leben -= 15
    mana -= 10
    tiefe += 1
print(f"Tiefe {tiefe}, Leben {leben}, Mana {mana}")

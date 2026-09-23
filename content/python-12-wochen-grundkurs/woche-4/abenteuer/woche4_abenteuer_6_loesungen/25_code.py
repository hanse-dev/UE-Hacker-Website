mana = 30
zauber_anzahl = 0
while mana >= 8:
    mana -= 8
    zauber_anzahl += 1
print(f"Zauber gewirkt: {zauber_anzahl}, Mana übrig: {mana}")

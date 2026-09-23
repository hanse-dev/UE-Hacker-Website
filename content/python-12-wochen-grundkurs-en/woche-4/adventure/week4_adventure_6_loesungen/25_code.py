mana = 30
spell_count = 0
while mana >= 8:
    mana -= 8
    spell_count += 1
print(f"Spells cast: {spell_count}, mana left: {mana}")

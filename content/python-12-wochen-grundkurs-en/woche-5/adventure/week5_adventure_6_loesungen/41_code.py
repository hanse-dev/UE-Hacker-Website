def is_spell_possible(mana_cost, current_mana):
    return current_mana >= mana_cost

print(f"Fireball: {is_spell_possible(30, 50)}")
print(f"Lightning: {is_spell_possible(40, 25)}")

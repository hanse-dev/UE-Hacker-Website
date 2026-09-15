# Example 2: Artifacts are immutable
spell_status = ("Active", "Stable", "Powerful")
print(f"Spell status: {spell_status}")

# Access works
print(f"Status: {spell_status[0]}")

# Modification does NOT work!
try:
    spell_status[0] = "Inactive"
except TypeError as e:
    print(f"Error: {e}")

# But artifacts inside lists can be replaced
spells = [
    ("Fireball", "Active"),
    ("Healing", "Stable"),
    ("Shield", "Powerful")
]
spells[1] = ("Healing", "Inactive")
print(f"\nSpells after change: {spells}")
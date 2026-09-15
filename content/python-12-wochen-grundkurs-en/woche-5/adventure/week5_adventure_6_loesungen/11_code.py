import random

# Step 1 – Greeting spell
def greet_wizard():
    print("Greetings, wizard apprentice!")
    print("Welcome to the School of Spell Formulas!")

greet_wizard()
greet_wizard()

# Step 2 – Mana calculation
def calculate_mana(level, base_mana):
    return level * base_mana

# Step 3 – Spell availability
def is_spell_possible(mana_cost, current_mana):
    return current_mana >= mana_cost

# Step 4 – Main block
mana = calculate_mana(5, 20)
print(f"Mana: {mana}")

if is_spell_possible(80, mana):
    print("Fireball is possible!")
else:
    print("Not enough mana for Fireball.")

if is_spell_possible(120, mana):
    print("Lightning Storm is possible!")
else:
    print("Not enough mana for Lightning Storm.")

# Bonus – random spell
def generate_spell():
    spells = ["Fireball", "Healing", "Shield", "Lightning", "Ice Nova"]
    return random.choice(spells)

print(f"Random spell: {generate_spell()}")
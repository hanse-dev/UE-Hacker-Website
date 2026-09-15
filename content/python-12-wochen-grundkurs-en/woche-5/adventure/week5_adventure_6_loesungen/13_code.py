import random

# Step 1 – Character basics
def create_character(name, hero_class, level):
    """Creates a character dictionary.
    
    Parameters:
        name (str): Name of the character
        hero_class (str): Class of the character (e.g. 'Wizard', 'Warrior')
        level (int): Current level of the character
    
    Returns:
        dict: Dictionary with name, hero_class and level
    """
    return {"name": name, "hero_class": hero_class, "level": level}

# Step 2 – Calculate health
def calculate_health(level, hero_class):
    base = {"Wizard": 50, "Rogue": 70, "Warrior": 100, "Healer": 80}
    base_health = base.get(hero_class, 75)
    return base_health + level * 10

# Step 3 – Create equipment
def generate_equipment(hero_class):
    sets = {
        "Wizard": ["Magic Staff", "Wizard Robe", "Spellbook"],
        "Warrior": ["Longsword", "Chain Armour", "Round Shield"],
        "Rogue": ["Dagger", "Leather Armour", "Throwing Knives"],
        "Healer": ["Healing Staff", "Robe", "Herb Bag"]
    }
    return sets.get(hero_class, ["Wooden Staff", "Ragged Robe"])

# Step 4 – Character sheet
def show_character_sheet(character, health, equipment):
    print("=" * 30)
    print("      CHARACTER SHEET")
    print("=" * 30)
    print(f"Name:    {character['name']}")
    print(f"Class:   {character['hero_class']}")
    print(f"Level:   {character['level']}")
    print(f"Health:  {health} HP")
    print("Equipment:")
    for item in equipment:
        print(f"  - {item}")
    print("=" * 30)

hero = create_character("Aldric", "Warrior", 7)
health = calculate_health(hero["level"], hero["hero_class"])
equipment = generate_equipment(hero["hero_class"])
show_character_sheet(hero, health, equipment)

# Bonus – random stats
hero["strength"] = random.randint(10, 30)
hero["intelligence"] = random.randint(5, 20)
print(f"Strength: {hero['strength']} | Intelligence: {hero['intelligence']}")
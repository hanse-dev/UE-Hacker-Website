class Hero:
    pass

hero = Hero()
hero.name = "Aria"
hero.level = 1
hero2 = Hero()
hero2.name = "Thorin"
hero2.level = 1
hero.level = 5
print(f"{hero.name}: {hero.level}")
print(f"{hero2.name}: {hero2.level}")

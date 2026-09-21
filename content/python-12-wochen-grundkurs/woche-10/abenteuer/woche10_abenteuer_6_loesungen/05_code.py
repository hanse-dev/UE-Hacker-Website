class Held:
    pass

held = Held()
held.name = "Aria"
held.level = 1
held2 = Held()
held2.name = "Thorin"
held2.level = 1
held.level = 5
print(f"{held.name}: {held.level}")
print(f"{held2.name}: {held2.level}")

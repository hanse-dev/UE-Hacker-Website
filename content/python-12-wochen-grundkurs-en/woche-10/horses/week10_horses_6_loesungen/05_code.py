class Horse:
    pass

horse = Horse()
horse.name = "Blitz"
horse.level = 1
horse2 = Horse()
horse2.name = "Stella"
horse2.level = 1
horse.level = 5
print(f"{horse.name}: {horse.level}")
print(f"{horse2.name}: {horse2.level}")

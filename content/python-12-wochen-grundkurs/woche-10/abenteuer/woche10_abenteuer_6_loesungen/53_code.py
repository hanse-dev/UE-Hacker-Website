class Held:
    def __init__(self, name, level=1, energie=100):
        self.name = name
        self.level = level
        self.energie = energie

gruppe = [Held("Aria", 15), Held("Thorin", 18), Held("Luna", 12)]
for h in gruppe:
    print(f"{h.name}: {h.level}")

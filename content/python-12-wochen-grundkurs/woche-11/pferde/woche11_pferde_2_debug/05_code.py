class tier:
    def __init__(name):
        self.name = name

class pferd(tier):
    def __init__(name, rasse):
        super().__init__(name)
        self.rasse = rasse

stormy = pferd("Stormy", "Islandpferd")
print(stormy.name)
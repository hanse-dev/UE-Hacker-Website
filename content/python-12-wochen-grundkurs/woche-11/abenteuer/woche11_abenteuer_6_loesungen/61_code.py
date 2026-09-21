class Held:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def kaempfe(self):
        print(f"{self.name} kämpft mit bloßen Händen.")

    def kraft(self):
        return 10

class Krieger(Held):
    def __init__(self, name, staerke=30):
        super().__init__(name)
        self.staerke = staerke

    def kaempfe(self):
        print(f"{self.name} schwingt das Schwert.")

    def kraft(self):
        return self.staerke

class Magier(Held):
    def __init__(self, name, mana=50):
        super().__init__(name)
        self.mana = mana

    def kaempfe(self):
        print(f"{self.name} wirft einen Feuerball.")

    def kraft(self):
        return self.mana

team = [Krieger("Aria"), Magier("Thorin"), Held("Luna")]
def staerkster(team):
    beste = team[0]
    for f in team:
        if f.kraft() > beste.kraft():
            beste = f
    return beste

print(f"Stärkster: {staerkster(team).name}")

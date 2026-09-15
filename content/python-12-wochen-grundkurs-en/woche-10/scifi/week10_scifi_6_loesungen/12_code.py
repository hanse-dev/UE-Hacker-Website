class Soldier:
    def __init__(self, name, rank="Recruit", unit="Standard"):
        self.name = name
        self.rank = rank
        self.unit = unit

    def introduce(self):
        print(f"⚔️ {self.name} | {self.rank} | Unit: {self.unit}")

    def promote(self, new_rank):
        self.rank = new_rank
        print(f"{self.name} was promoted to: {self.rank}!")

shepard = Soldier("Shepard", "Commander", "N7")
vasquez = Soldier("Vasquez", "Sergeant", "Alpha")
hicks = Soldier("Hicks", unit="Bravo")

print("=== Space Marines ===")
for s in [shepard, vasquez, hicks]:
    s.introduce()

hicks.promote("Private First Class")
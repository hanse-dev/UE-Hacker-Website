# Solution Suggestion Boss Quest 1 – The Rank Hierarchy

# Step 1: Base class
class CrewMember:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def show_permissions(self):
        print(f"{self.name} ({self.rank}): Basic fleet rights.")

    def __str__(self):
        return f"[{self.rank}] {self.name}"

# Step 2: Ranks
class Cadet(CrewMember):
    def __init__(self, name):
        super().__init__(name, "Cadet")

    def show_permissions(self):
        print(f"{self.name} ({self.rank}): Access to training rooms and dormitories. No weapon access.")

class Officer(CrewMember):
    def __init__(self, name):
        super().__init__(name, "Officer")

    def show_permissions(self):
        print(f"{self.name} ({self.rank}): Access to the bridge, armory and command rooms.")

class Captain(CrewMember):
    def __init__(self, name):
        super().__init__(name, "Captain")

    def show_permissions(self):
        print(f"{self.name} ({self.rank}): Full ship control – course setting, combat orders, emergency protocols.")

# Step 3: Briefing
crew = [
    Cadet("Nova"),
    Officer("Vega"),
    Captain("Commander Zara")
]

print("=== FLEET BRIEFING ===")
for member in crew:
    print(member)                    # __str__
    member.show_permissions()
    print()
class CrewMember:
    def __init__(self, name, rank, speciality):
        self.name = name
        self.rank = rank
        self.speciality = speciality

    def introduce(self):
        print(f"👤 {self.name} | {self.rank} | Speciality: {self.speciality}")

    def mission(self, assignment):
        print(f"{self.name} takes on mission: {assignment}")

class Crew:
    def __init__(self):
        self.members = []

    def add(self, member):
        self.members.append(member)

    def show_all(self):
        print(f"\n=== Crew ({len(self.members)} members) ===")
        for m in self.members:
            m.introduce()

crew = Crew()
crew.add(CrewMember("Zara", "Captain", "Navigation"))
crew.add(CrewMember("Orion", "Doctor", "Xenobiology"))
crew.add(CrewMember("Maya", "Engineer", "Propulsion Systems"))
crew.add(CrewMember("Kai", "Pilot", "Combat Manoeuvres"))
crew.show_all()
crew.members[0].mission("Exploration of Sector 7")
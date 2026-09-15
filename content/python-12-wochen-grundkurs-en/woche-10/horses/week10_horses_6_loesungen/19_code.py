class RidingStudent:
    def __init__(self, name, level=1, favourite_horse="None"):
        self.name = name
        self.level = level
        self.favourite_horse = favourite_horse

    def introduce(self):
        print(f"👤 {self.name} | Level {self.level} | Horse: {self.favourite_horse}")

    def lesson(self, topic):
        print(f"{self.name} is learning: {topic}")
        self.level += 1

class RidingSchool:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enrol(self, student):
        self.students.append(student)
        print(f"{student.name} enrolled at '{self.name}'.")

    def show_all(self):
        print(f"\n=== {self.name} ({len(self.students)} students) ===")
        for s in self.students:
            s.introduce()

school = RidingSchool("Sonnental Riding School")
school.enrol(RidingStudent("Lisa", 3, "Thunder"))
school.enrol(RidingStudent("Tom", 1))
school.enrol(RidingStudent("Sarah", 5, "Luna"))
school.show_all()
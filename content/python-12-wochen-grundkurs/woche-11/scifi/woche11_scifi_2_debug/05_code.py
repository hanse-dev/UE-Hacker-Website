class maschine:
    def __init__(id):
        self.id = id

class android(maschine):
    def __init__(id, name):
        super().__init__(id)
        self.name = name

unit7 = android("007", "Seven")
print(unit7.id)
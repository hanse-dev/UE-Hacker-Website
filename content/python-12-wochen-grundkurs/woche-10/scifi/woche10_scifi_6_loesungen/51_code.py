class Werkzeug:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

    def info(self):
        return f"{self.name} ({self.wert})"

print(Werkzeug("Plasmalaser", 50).info())
print(Werkzeug("Ionenblaster", 35).info())

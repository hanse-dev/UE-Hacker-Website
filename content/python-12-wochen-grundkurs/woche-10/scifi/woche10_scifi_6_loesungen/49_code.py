class Werkzeug:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

a = Werkzeug("Plasmalaser", 50)
b = Werkzeug("Ionenblaster", 35)
print(f"Zusammen: {a.wert + b.wert}")

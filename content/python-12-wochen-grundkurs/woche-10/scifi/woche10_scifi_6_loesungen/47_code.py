class Werkzeug:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

werkzeug = Werkzeug("Plasmalaser", 50)
print(f"{werkzeug.name}: {werkzeug.wert}")

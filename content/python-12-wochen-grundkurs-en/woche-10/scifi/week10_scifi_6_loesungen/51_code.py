class Tool:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def info(self):
        return f"{self.name} ({self.value})"

print(Tool("Plasma laser", 50).info())
print(Tool("Ion blaster", 35).info())

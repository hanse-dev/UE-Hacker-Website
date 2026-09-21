class Saddle:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def info(self):
        return f"{self.name} ({self.value})"

print(Saddle("Show saddle", 50).info())
print(Saddle("Riding blanket", 35).info())

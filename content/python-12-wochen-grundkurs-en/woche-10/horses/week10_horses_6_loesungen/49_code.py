class Saddle:
    def __init__(self, name, value):
        self.name = name
        self.value = value

a = Saddle("Show saddle", 50)
b = Saddle("Riding blanket", 35)
print(f"Together: {a.value + b.value}")

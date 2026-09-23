class Saddle:
    def __init__(self, name, value):
        self.name = name
        self.value = value

saddle = Saddle("Show saddle", 50)
print(f"{saddle.name}: {saddle.value}")

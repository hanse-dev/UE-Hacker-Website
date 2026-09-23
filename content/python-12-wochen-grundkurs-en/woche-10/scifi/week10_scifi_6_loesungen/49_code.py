class Tool:
    def __init__(self, name, value):
        self.name = name
        self.value = value

a = Tool("Plasma laser", 50)
b = Tool("Ion blaster", 35)
print(f"Together: {a.value + b.value}")

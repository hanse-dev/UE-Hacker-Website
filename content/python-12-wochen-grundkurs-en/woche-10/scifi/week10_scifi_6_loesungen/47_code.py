class Tool:
    def __init__(self, name, value):
        self.name = name
        self.value = value

tool = Tool("Plasma laser", 50)
print(f"{tool.name}: {tool.value}")

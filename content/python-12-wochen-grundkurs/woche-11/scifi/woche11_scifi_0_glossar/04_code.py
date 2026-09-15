class Raumschiff:
    def __init__(self, name):
        self.name = name

    def fähigkeit(self):
        return "Fliegt durch den Weltraum"

    def __str__(self):
        return f"Schiff: {self.name}"

# Vererbung
class Kriegsschiff(Raumschiff):
    def __init__(self, name, waffen):
        super().__init__(name)
        self.waffen = waffen

    def fähigkeit(self):   # Polymorphismus
        return f"Kämpft mit {self.waffen} Waffen!"

enterprise = Raumschiff("Enterprise")
defiant = Kriegsschiff("Defiant", waffen=12)

print(enterprise)                  # Schiff: Enterprise
print(enterprise.fähigkeit())      # Fliegt durch den Weltraum
print(defiant.fähigkeit())         # Kämpft mit 12 Waffen!

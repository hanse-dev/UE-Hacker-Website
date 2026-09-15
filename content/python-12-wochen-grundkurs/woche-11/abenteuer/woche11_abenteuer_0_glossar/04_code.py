class Held:
    def __init__(self, name):
        self.name = name

    def fähigkeit(self):
        return "Kämpft mit dem Schwert"

    def __str__(self):
        return f"Held: {self.name}"

# Vererbung
class Magier(Held):
    def __init__(self, name, mana):
        super().__init__(name)
        self.mana = mana

    def fähigkeit(self):   # Polymorphismus
        return f"Wirkt Zauber (Mana: {self.mana})"

aria = Held("Aria")
gandalf = Magier("Gandalf", mana=100)

print(aria)                  # Held: Aria
print(aria.fähigkeit())      # Kämpft mit dem Schwert
print(gandalf.fähigkeit())   # Wirkt Zauber (Mana: 100)

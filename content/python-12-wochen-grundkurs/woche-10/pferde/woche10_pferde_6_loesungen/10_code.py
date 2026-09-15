class Pferd:
    def __init__(self, name, rasse, alter, geschlecht):
        self.name = name
        self.rasse = rasse
        self.alter = alter
        self.geschlecht = geschlecht

    def vorstellen(self):
        print(f"Ich bin {self.name}, eine {self.rasse}, {self.alter} Jahre alt.")

# Drei Pferde erstellen
p1 = Pferd("Thunder", "Hannoveraner", 6, "Hengst")
p2 = Pferd("Luna", "Haflinger", 4, "Stute")
p3 = Pferd("Storm", "Arabisches Vollblut", 8, "Wallach")

for pferd in [p1, p2, p3]:
    pferd.vorstellen()

print(f"\nThunders Rasse: {p1.rasse}")
print(f"Lunas Alter: {p2.alter}")
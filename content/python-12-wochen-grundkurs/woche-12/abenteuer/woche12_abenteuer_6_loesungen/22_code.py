# Lösungsvorschlag Boss-Quest 3 – Die Zufalls-Kunst
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Magische Zufalls-Kunst")

# Bonus: Klasse MagischerZeichner
class MagischerZeichner:
    def __init__(self):
        self.stift = turtle.Turtle()
        self.stift.speed(0)
        self.stift.hideturtle()
        self.magische_farben = [
            "gold", "cyan", "magenta", "orange", "lime",
            "purple", "pink", "aquamarine", "tomato", "orchid"
        ]

    # Schritt 1: Bausteine
    def zeichne_zauberstern(self, x, y, groesse, farbe):
        self.stift.penup()
        self.stift.goto(x, y)
        self.stift.pendown()
        self.stift.color(farbe)
        self.stift.fillcolor(farbe)
        self.stift.begin_fill()
        for _ in range(5):
            self.stift.forward(groesse)
            self.stift.right(144)
        self.stift.end_fill()

    def zeichne_zauberkreis(self, x, y, radius, farbe):
        self.stift.penup()
        self.stift.goto(x, y - radius)
        self.stift.pendown()
        self.stift.color(farbe)
        self.stift.fillcolor(farbe)
        self.stift.begin_fill()
        self.stift.circle(radius)
        self.stift.end_fill()

    def zeichne_spirale(self, x, y, farbe):
        self.stift.penup()
        self.stift.goto(x, y)
        self.stift.pendown()
        self.stift.color(farbe)
        for i in range(20):
            self.stift.forward(i * 3)
            self.stift.right(45)

    # Schritt 2: Zufalls-Kunst
    def erschaffe_kunstwerk(self, anzahl=12):
        formen = ["stern", "kreis", "spirale"]
        for _ in range(anzahl):
            x = random.randint(-250, 250)
            y = random.randint(-180, 180)
            farbe = random.choice(self.magische_farben)
            form = random.choice(formen)
            if form == "stern":
                groesse = random.randint(20, 60)
                self.zeichne_zauberstern(x, y, groesse, farbe)
            elif form == "kreis":
                radius = random.randint(10, 40)
                self.zeichne_zauberkreis(x, y, radius, farbe)
            else:
                self.zeichne_spirale(x, y, farbe)

# Schritt 3: Kunstwerk erschaffen
kuenstler = MagischerZeichner()
kuenstler.erschaffe_kunstwerk(anzahl=15)

# Signatur
kuenstler.stift.penup()
kuenstler.stift.goto(0, -215)
kuenstler.stift.color("gold")
kuenstler.stift.write("✨ Zufalls-Kunst by MagischerZeichner ✨", align="center", font=("Arial", 10, "italic"))

print()
print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Meister der Zeichenrollen besiegt!")
print("⭐ Titel erhalten: Magier der visuellen Künste")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 12 gemeistert!")

turtle.done()
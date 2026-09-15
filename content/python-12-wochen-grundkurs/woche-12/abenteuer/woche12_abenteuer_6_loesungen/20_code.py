# Lösungsvorschlag Boss-Quest 2 – Das animierte Zaubersiegel
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Zaubersiegel")

stift = turtle.Turtle()
stift.speed(6)

# Schritt 1: Grundform-Funktionen
def zeichne_stern(stift, x, y, groesse, farbe):
    stift.penup()
    stift.goto(x, y)
    stift.pendown()
    stift.color(farbe)
    stift.fillcolor(farbe)
    stift.begin_fill()
    for _ in range(5):
        stift.forward(groesse)
        stift.right(144)
    stift.end_fill()

def zeichne_kreis(stift, x, y, radius, farbe):
    stift.penup()
    stift.goto(x, y - radius)
    stift.pendown()
    stift.color(farbe)
    stift.circle(radius)

def zeichne_hexagon(stift, x, y, groesse, farbe):
    stift.penup()
    stift.goto(x, y)
    stift.pendown()
    stift.color(farbe)
    for _ in range(6):
        stift.forward(groesse)
        stift.right(60)

# Schritt 2: Siegel zusammensetzen
# Äußerer Kreis
zeichne_kreis(stift, 0, 0, 150, "gold")

# Mittleres Muster: Hexagon
zeichne_hexagon(stift, -80, -40, 80, "cyan")

# Innerer Kern: Stern
zeichne_stern(stift, -30, -20, 60, "red")

# Schritt 3: Farb-Variationen (Bonus: random)
magische_farben = ["purple", "blue", "lime", "orange", "pink"]
for i in range(6):
    farbe = random.choice(magische_farben)
    zeichne_kreis(stift, 0, 0, 20 + i * 20, farbe)

# Zentrum
zeichne_stern(stift, -15, -10, 30, "white")

stift.penup()
stift.goto(0, -180)
stift.color("gold")
stift.write("⭐ Zaubersiegel Aktiviert ⭐", align="center", font=("Arial", 12, "bold"))

stift.hideturtle()
turtle.done()
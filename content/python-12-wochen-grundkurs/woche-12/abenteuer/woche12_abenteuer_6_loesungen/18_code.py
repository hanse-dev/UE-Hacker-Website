# Lösungsvorschlag Boss-Quest 1 – Die Landkarte von Pyralia
import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Karte von Pyralia")

karte = turtle.Turtle()
karte.speed(0)

def zeichne_rahmen(stift):
    stift.penup()
    stift.goto(-280, -200)
    stift.pendown()
    stift.color("brown")
    stift.width(4)
    for _ in range(2):
        stift.forward(560)
        stift.left(90)
        stift.forward(400)
        stift.left(90)
    stift.width(1)

def zeichne_ort(stift, x, y, farbe, name):
    stift.penup()
    stift.goto(x, y - 15)
    stift.pendown()
    stift.color(farbe)
    stift.fillcolor(farbe)
    stift.begin_fill()
    stift.circle(15)
    stift.end_fill()
    stift.penup()
    stift.goto(x, y - 35)
    stift.color("black")
    stift.write(name, align="center", font=("Arial", 9, "bold"))

def zeichne_weg(stift, x1, y1, x2, y2):
    stift.penup()
    stift.goto(x1, y1)
    stift.pendown()
    stift.color("sienna")
    stift.width(2)
    stift.goto(x2, y2)
    stift.width(1)

# Schritt 1: Hintergrund
zeichne_rahmen(karte)

# Schritt 2: Orte
orte = [
    (-150, 80, "royalblue", "Kristallsee"),
    (100, 100, "darkgreen", "Zauberwald"),
    (0, -80, "gray", "Drachenberg"),
    (-100, -120, "gold", "Goldstadt")
]
for x, y, farbe, name in orte:
    zeichne_ort(karte, x, y, farbe, name)

# Schritt 3: Wege zwischen Orten
zeichne_weg(karte, -150, 80, 100, 100)
zeichne_weg(karte, 100, 100, 0, -80)
zeichne_weg(karte, 0, -80, -100, -120)
zeichne_weg(karte, -100, -120, -150, 80)

# Kompass
karte.penup()
karte.goto(210, 130)
karte.color("black")
karte.write("N", align="center", font=("Arial", 12, "bold"))
karte.goto(210, 90)
karte.write("S", align="center", font=("Arial", 12, "bold"))
karte.goto(230, 110)
karte.write("O", align="center", font=("Arial", 12, "bold"))
karte.goto(190, 110)
karte.write("W", align="center", font=("Arial", 12, "bold"))

karte.hideturtle()
turtle.done()
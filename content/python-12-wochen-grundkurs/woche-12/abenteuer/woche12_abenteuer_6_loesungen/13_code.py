# Lösungsvorschlag Mission 2 – Der Zauberhut des Magiers
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Zauberhut des Magiers")

hut = turtle.Turtle()
hut.speed(3)

# Schritt 1: Zylinder (Hauptteil des Hutes)
hut.penup()
hut.goto(-50, -50)
hut.pendown()
hut.color("purple")
hut.fillcolor("purple")
hut.begin_fill()
for breite, hoehe in [(100, 0), (0, 150), (-100, 0), (0, -150)]:
    hut.forward(breite if breite != 0 else hoehe)
    hut.left(90)
# einfacher mit goto:
hut.end_fill()

# Krempe (breiteres Rechteck unten)
hut.penup()
hut.goto(-80, -50)
hut.pendown()
hut.color("blue")
hut.fillcolor("blue")
hut.begin_fill()
for _ in range(2):
    hut.forward(160)
    hut.left(90)
    hut.forward(20)
    hut.left(90)
hut.end_fill()

# Schritt 2: Stern-Verzierung
hut.penup()
hut.goto(10, 30)
hut.pendown()
hut.color("yellow")
hut.fillcolor("yellow")
hut.begin_fill()
for _ in range(5):
    hut.forward(20)
    hut.right(144)
hut.end_fill()

# Schritt 3: Beschriftung
hut.penup()
hut.goto(0, -100)
hut.color("white")
hut.write("🌟 Zauberhut von Merlin", align="center", font=("Arial", 11, "bold"))

hut.hideturtle()
turtle.done()
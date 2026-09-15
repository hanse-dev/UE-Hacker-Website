# Beispiel 1: Hindernisse zeichnen
import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

# Hindernis-Zeichner
hindernis = turtle.Turtle()
hindernis.speed(3)
hindernis.color("brown")

def zeichne_hindernis(x, y, höhe):
    hindernis.penup()
    hindernis.goto(x, y)
    hindernis.pendown()
    hindernis.begin_fill()
    hindernis.fillcolor("saddlebrown")
    for _ in range(2):
        hindernis.forward(40)
        hindernis.left(90)
        hindernis.forward(höhe)
        hindernis.left(90)
    hindernis.end_fill()

# Zeichne mehrere Hindernisse
zeichne_hindernis(-150, -100, 60)
zeichne_hindernis(-50, -100, 80)
zeichne_hindernis(50, -100, 70)
zeichne_hindernis(150, -100, 90)

turtle.done()
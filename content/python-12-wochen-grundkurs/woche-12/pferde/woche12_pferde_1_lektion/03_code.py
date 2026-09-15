# Beispiel 1: Eine einfache Reitbahn
import turtle

# Erstelle das Turnier-Feld
screen = turtle.Screen()
screen.title("Turnierplatz von Pyralia")
screen.bgcolor("green")

# Erstelle den Bahn-Zeichner
bahn = turtle.Turtle()
bahn.speed(5)
bahn.color("white")
bahn.pensize(3)

# Zeichne die äußere Bahn
bahn.penup()
bahn.goto(-200, -150)
bahn.pendown()
for _ in range(2):
    bahn.forward(400)
    bahn.left(90)
    bahn.forward(300)
    bahn.left(90)

# Mittellinie
bahn.penup()
bahn.goto(0, -150)
bahn.pendown()
bahn.goto(0, 150)

turtle.done()
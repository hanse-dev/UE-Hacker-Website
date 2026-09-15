# Beispiel 1: Weltraum mit Sternen
import turtle
import random

# Erstelle das Hologramm-Fenster
screen = turtle.Screen()
screen.title("Hologramm-Projektor Nebula-7")
screen.bgcolor("black")
screen.setup(800, 600)

# Erstelle Sternen-Zeichner
stern = turtle.Turtle()
stern.speed(0)
stern.hideturtle()

# Zeichne zufällige Sterne
def zeichne_stern(x, y, größe):
    stern.penup()
    stern.goto(x, y)
    stern.pendown()
    stern.color("white")
    stern.begin_fill()
    for _ in range(5):
        stern.forward(größe)
        stern.right(144)
    stern.end_fill()

# Erstelle 100 zufällige Sterne
for _ in range(100):
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    größe = random.randint(1, 5)
    zeichne_stern(x, y, größe)

turtle.done()
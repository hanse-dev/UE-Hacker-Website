# Beispiel 1: Ein einfaches Raumschiff
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

# Raumschiff-Zeichner
schiff = turtle.Turtle()
schiff.speed(3)
schiff.color("silver")
schiff.pensize(2)

def zeichne_raumschiff(x, y):
    schiff.penup()
    schiff.goto(x, y)
    schiff.pendown()
    schiff.fillcolor("gray")
    schiff.begin_fill()
    
    # Hauptkörper
    schiff.forward(60)
    schiff.right(120)
    schiff.forward(40)
    schiff.right(60)
    schiff.forward(40)
    schiff.right(120)
    schiff.forward(60)
    
    schiff.end_fill()

# Zeichne das Raumschiff
zeichne_raumschiff(0, 0)

# Füge Fenster hinzu
schiff.penup()
schiff.goto(20, -10)
schiff.pendown()
schiff.color("cyan")
schiff.begin_fill()
schiff.circle(10)
schiff.end_fill()

turtle.done()
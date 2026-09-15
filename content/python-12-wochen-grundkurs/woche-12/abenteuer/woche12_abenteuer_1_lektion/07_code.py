# Beispiel 1: Magische Farben und Füllungen
import turtle

screen = turtle.Screen()
screen.bgcolor("darkblue")
pen = turtle.Turtle()
pen.speed(3)

# Magischer Stern
pen.color("yellow", "orange")
pen.begin_fill()
for _ in range(5):
    pen.forward(100)
    pen.right(144)
pen.end_fill()

# Magischer Kreis
pen.penup()
pen.goto(150, 0)
pen.pendown()
pen.color("cyan", "lightblue")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

turtle.done()
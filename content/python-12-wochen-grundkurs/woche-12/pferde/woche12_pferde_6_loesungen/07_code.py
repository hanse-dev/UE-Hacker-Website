# Problem: end_fill() fehlt
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

bahn = turtle.Turtle()
bahn.speed(0)
bahn.color("red")
bahn.fillcolor("blue")
bahn.begin_fill()
bahn.circle(50)
bahn.end_fill()  # Fehlende Zeile hinzugefügt
turtle.done()
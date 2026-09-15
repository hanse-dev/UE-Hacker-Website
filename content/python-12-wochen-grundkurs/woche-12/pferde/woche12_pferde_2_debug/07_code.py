# Warum ist der Kreis nicht gefüllt?
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

bahn = turtle.Turtle()
bahn.speed(0)
bahn.color("red")
bahn.fillcolor("blue")
bahn.begin_fill()
bahn.circle(50)
# Was fehlt am Ende?
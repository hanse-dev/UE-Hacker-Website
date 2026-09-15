# Beispiel 1: Grundlegende Bewegungen
import turtle

screen = turtle.Screen()
screen.bgcolor("navy")
pen = turtle.Turtle()
pen.speed(5)
pen.color("gold")

# Ein magisches Quadrat
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# Ein magisches Dreieck
pen.penup()
pen.goto(-150, 0)
pen.pendown()
for _ in range(3):
    pen.forward(100)
    pen.left(120)

turtle.done()
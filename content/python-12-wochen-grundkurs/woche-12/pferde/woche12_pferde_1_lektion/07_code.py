# Beispiel 1: Pferd auf der Bahn
import turtle
import time

screen = turtle.Screen()
screen.bgcolor("green")

# Erstelle ein Pferd
pferd = turtle.Turtle()
pferd.shape("turtle")  # Tempär, bis wir eine bessere Form haben
pferd.color("black")
pferd.shapesize(2, 1.5)
pferd.penup()

# Startposition
pferd.goto(-180, 0)

# Pferd bewegen
for _ in range(10):
    pferd.forward(40)
    time.sleep(0.5)

turtle.done()
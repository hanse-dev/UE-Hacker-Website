# Example 3: Horse on the track
import turtle
import time

screen = turtle.Screen()
screen.bgcolor("green")

horse = turtle.Turtle()
horse.shape("turtle")
horse.color("black")
horse.shapesize(2, 1.5)
horse.penup()

horse.goto(-180, 0)

for _ in range(10):
    horse.forward(40)
    time.sleep(0.5)

turtle.done()
# Example 1: Basic movements
import turtle

screen = turtle.Screen()
screen.bgcolor("navy")
pen = turtle.Turtle()
pen.speed(5)
pen.color("gold")

# A magic square
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# A magic triangle
pen.penup()
pen.goto(-150, 0)
pen.pendown()
for _ in range(3):
    pen.forward(100)
    pen.left(120)

turtle.done()
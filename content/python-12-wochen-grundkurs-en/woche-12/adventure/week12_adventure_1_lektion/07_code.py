# Example 1: Magic colours and fills
import turtle

screen = turtle.Screen()
screen.bgcolor("darkblue")
pen = turtle.Turtle()
pen.speed(3)

# Magic star
pen.color("yellow", "orange")
pen.begin_fill()
for _ in range(5):
    pen.forward(100)
    pen.right(144)
pen.end_fill()

# Magic circle
pen.penup()
pen.goto(150, 0)
pen.pendown()
pen.color("cyan", "lightblue")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

turtle.done()
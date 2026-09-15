# Problem: end_fill() is missing
import turtle

pen = turtle.Turtle()
pen.color("red", "darkred")
pen.begin_fill()
for _ in range(5):
    pen.forward(100)
    pen.right(144)
pen.end_fill()  # Missing line added
turtle.done()
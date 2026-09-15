# Problem: turtle.done() is missing at the end
import turtle

pen = turtle.Turtle()
pen.speed(1)
pen.color("white")
pen.forward(100)
turtle.done()  # Missing line added
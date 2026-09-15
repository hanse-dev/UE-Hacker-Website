# Problem: black stars on white background – fix: use black background
import turtle

screen = turtle.Screen()
screen.bgcolor("black")  # Fixed: black background

star = turtle.Turtle()
star.color("white")  # Now visible on black background
star.begin_fill()
star.fillcolor("white")
for _ in range(5):
    star.forward(20)
    star.right(144)
star.end_fill()
turtle.done()
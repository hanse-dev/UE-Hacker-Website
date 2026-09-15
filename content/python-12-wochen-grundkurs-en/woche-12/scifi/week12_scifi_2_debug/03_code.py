# Why are the stars invisible?
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

star = turtle.Turtle()
star.color("white")
star.begin_fill()
star.fillcolor("white")
for _ in range(5):
    star.forward(20)
    star.right(144)
star.end_fill()
turtle.done()
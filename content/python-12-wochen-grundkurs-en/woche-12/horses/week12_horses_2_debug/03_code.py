# Why can't you see the obstacle?
import turtle

obstacle = turtle.Turtle()
obstacle.color("brown")
obstacle.penup()
obstacle.goto(-50, -50)
# What is missing here?
obstacle.forward(100)
obstacle.left(90)
obstacle.forward(80)
turtle.done()
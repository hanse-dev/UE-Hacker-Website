# Problem: pendown() is missing
import turtle

obstacle = turtle.Turtle()
obstacle.color("brown")
obstacle.penup()
obstacle.goto(0, 0)
obstacle.pendown()  # Missing line added
obstacle.circle(50)
turtle.done()
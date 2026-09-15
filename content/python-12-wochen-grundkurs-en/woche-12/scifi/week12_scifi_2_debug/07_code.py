# Why is the planet ring invisible?
import turtle

screen = turtle.Screen()
screen.bgcolor("white")  # White background

planet = turtle.Turtle()
planet.speed(0)
planet.fillcolor("tan")
planet.begin_fill()
planet.circle(30)
planet.end_fill()

# Ring
planet.penup()
planet.goto(0, -40)
planet.pendown()
planet.color("white")
planet.width(4)
planet.circle(45)
turtle.done()
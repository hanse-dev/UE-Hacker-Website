# Problem: ring was white on white background – fix: use a visible colour
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

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
planet.color("gray")  # Fixed: use a visible colour
planet.width(4)
planet.circle(45)
turtle.done()
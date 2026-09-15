# Warum ist der Ring unsichtbar?
import turtle

planet = turtle.Turtle()
planet.color("blue")
planet.penup()
planet.goto(0, -30)
planet.pendown()
planet.circle(30)
# Jetzt der Ring:
planet.penup()
planet.goto(0, -55)
planet.color("white")
planet.width(8)
planet.pendown()
planet.circle(55)
turtle.done()
# Beispiel 1: Planetensystem
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

# Planeten-Zeichner
planet = turtle.Turtle()
planet.speed(5)
planet.hideturtle()

# Sonne
planet.penup()
planet.goto(0, 0)
planet.pendown()
planet.color("yellow")
planet.begin_fill()
planet.fillcolor("orange")
planet.circle(50)
planet.end_fill()

# Planet 1
planet.penup()
planet.goto(150, 0)
planet.pendown()
planet.color("blue")
planet.begin_fill()
planet.fillcolor("lightblue")
planet.circle(20)
planet.end_fill()

# Planet 2 mit Ring
planet.penup()
planet.goto(-150, 0)
planet.pendown()
planet.color("brown")
planet.begin_fill()
planet.fillcolor("tan")
planet.circle(30)
planet.end_fill()

# Ring um Planet 2
planet.penup()
planet.goto(-150, -30)
planet.pendown()
planet.color("gray")
planet.width(3)
planet.circle(30, 360)

turtle.done()
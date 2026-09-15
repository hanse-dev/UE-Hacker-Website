# Problem: pendown() fehlt
import turtle

hindernis = turtle.Turtle()
hindernis.color("brown")
hindernis.penup()
hindernis.goto(0, 0)
hindernis.pendown()  # Fehlende Zeile
hindernis.circle(50)
turtle.done()
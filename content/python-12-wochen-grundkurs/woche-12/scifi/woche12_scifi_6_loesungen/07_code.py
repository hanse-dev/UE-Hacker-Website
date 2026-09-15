# Problem: Ring ist weiß auf weißem Hintergrund (unsichtbar)
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
planet.color("gold")  # sichtbare Farbe statt weiß
planet.width(8)
planet.pendown()
planet.circle(55)
turtle.done()

# Problem: turtle.done() fehlt
import turtle

schiff = turtle.Turtle()
schiff.shape("turtle")
schiff.color("red")
schiff.penup()  # Stift heben
schiff.goto(-100, 0)
schiff.forward(200)
turtle.done()  # Fehlende Zeile
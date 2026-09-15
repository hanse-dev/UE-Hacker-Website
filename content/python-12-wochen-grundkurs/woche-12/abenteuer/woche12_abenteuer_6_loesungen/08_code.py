# Problem: turtle.done() fehlt am Ende
import turtle

pen = turtle.Turtle()
pen.speed(1)  # Langsam genug zum Sehen
pen.color("white")
pen.forward(100)
turtle.done()  # Fehlende Zeile hinzugefügt
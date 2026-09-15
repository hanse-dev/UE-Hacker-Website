# Problem: end_fill() fehlt
import turtle

pen = turtle.Turtle()
pen.color("red", "darkred")  # Füllfarbe hinzufügen
pen.begin_fill()
for _ in range(5):
    pen.forward(100)
    pen.right(144)
pen.end_fill()  # Fehlende Zeile hinzugefügt
turtle.done()
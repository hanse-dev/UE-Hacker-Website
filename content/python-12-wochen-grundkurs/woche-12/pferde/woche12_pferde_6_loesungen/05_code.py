# Problem: penup() für Bewegung nutzen
import turtle

pferd = turtle.Turtle()
pferd.shape("turtle")
pferd.penup()  # Stift heben für Bewegung
pferd.goto(-100, 0)
pferd.forward(100)  # Jetzt funktioniert es
turtle.done()
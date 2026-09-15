# Problem: penup() must be called before goto()
import turtle

horse = turtle.Turtle()
horse.shape("turtle")
horse.penup()  # Lift pen before moving
horse.goto(-100, 0)
horse.forward(100)
turtle.done()
# Problem: penup() must be called before goto()
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

ship = turtle.Turtle()
ship.color("cyan")
ship.penup()  # Lift pen before moving
ship.goto(-100, 0)
ship.forward(200)
turtle.done()
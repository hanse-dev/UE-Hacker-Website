# Problem: end_fill() is missing
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

arena = turtle.Turtle()
arena.speed(0)
arena.color("red")
arena.fillcolor("blue")
arena.begin_fill()
arena.circle(50)
arena.end_fill()  # Missing line added
turtle.done()
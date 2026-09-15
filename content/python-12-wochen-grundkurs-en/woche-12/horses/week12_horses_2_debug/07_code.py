# Why is the circle not filled?
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

arena = turtle.Turtle()
arena.speed(0)
arena.color("red")
arena.fillcolor("blue")
arena.begin_fill()
arena.circle(50)
# What is missing at the end?
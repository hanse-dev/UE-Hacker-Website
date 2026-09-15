# Example 1: A simple riding arena
import turtle

screen = turtle.Screen()
screen.title("Tournament Ground")
screen.bgcolor("green")

arena = turtle.Turtle()
arena.speed(5)
arena.color("white")
arena.pensize(3)

# Draw outer arena
arena.penup()
arena.goto(-200, -150)
arena.pendown()
for _ in range(2):
    arena.forward(400)
    arena.left(90)
    arena.forward(300)
    arena.left(90)

# Centre line
arena.penup()
arena.goto(0, -150)
arena.pendown()
arena.goto(0, 150)

turtle.done()
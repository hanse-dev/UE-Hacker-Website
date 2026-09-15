# Example 1: Space background with random stars
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Nebula-7 Star Field")

star = turtle.Turtle()
star.speed(0)
star.color("white")
star.hideturtle()

def draw_star(x, y, size):
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.begin_fill()
    star.fillcolor("white")
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()

# Draw 100 random stars
for _ in range(100):
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    size = random.randint(3, 10)
    draw_star(x, y, size)

turtle.done()
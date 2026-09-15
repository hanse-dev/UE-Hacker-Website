import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Magic Seal")

pen = turtle.Turtle()
pen.speed(6)

def draw_star(pen, x, y, size, colour):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(colour)
    pen.fillcolor(colour)
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()

def draw_circle(pen, x, y, radius, colour):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(colour)
    pen.circle(radius)

def draw_hexagon(pen, x, y, size, colour):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(colour)
    for _ in range(6):
        pen.forward(size)
        pen.right(60)

draw_circle(pen, 0, 0, 150, "gold")
draw_hexagon(pen, -80, -40, 80, "cyan")
draw_star(pen, -30, -20, 60, "red")

magic_colours = ["purple", "blue", "lime", "orange", "pink"]
for i in range(6):
    colour = random.choice(magic_colours)
    draw_circle(pen, 0, 0, 20 + i * 20, colour)

draw_star(pen, -15, -10, 30, "white")

pen.penup()
pen.goto(0, -180)
pen.color("gold")
pen.write("⭐ Magic Seal Activated ⭐", align="center", font=("Arial", 12, "bold"))

pen.hideturtle()
turtle.done()